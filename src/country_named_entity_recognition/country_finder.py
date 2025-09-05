"""
MIT License

Copyright (c) 2023 Fast Data Science Ltd (https://fastdatascience.com)

Maintainer: Thomas Wood

Tutorial at https://fastdatascience.com/country-named-entity-recognition/

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import operator
import re

import pycountry

extra_synonyms = {"VN": {"Vietnam"}, "US": {"USA", "the US", r"U.S", r"U.S."}, "CZ": {"Czech Rep", "Czech Republic"},
                  "AE": {"UAE", r"U.A.E."},
                  "KR": {"Korea", "Republic of Korea"}, "KP": {"North Korea", "Democratic People's Republic of Korea"},
                  "CI": {"Ivory Coast"}, "CD": {"Congo, The Democratic Republic", "Congo, Democratic Republic",
                                                "Democratic Republic of the Congo",
                                                "Democratic Republic of Congo", "DR Congo", "DRC"},
                  "CV": {"Cape Verde"}, "SH": {"St. Helena", "St Helena"},
                  "GB": {"Britain", "United Kingdom", "UK", r"U.K", r"U.K."},
                  "RU": {"Russia"}, "VA": {"Holy See"}, "BN": {"Brunei"}, "LA": {"Laos"},
                  "VG": {"British Virgin Islands", "Virgin Islands (British)", "Virgin Islands, British"},
                  "VI": {"Virgin Islands (US)", "Virgin Islands (U.S.)", "Virgin Islands, US", "Virgin Islands, U.S."},
                  "SY": {"Syria"}, "GE": {"Republic of Georgia"},
                  'GM': {'gambia, republic of', 'gambia republic', 'republic of gambia', 'republic of the gambia'},
                  "NL": {"Nerlands"}, "IR": {"Iran"}, "AE": {"UAE", "U.A.E."},
                  "MK": {"Macedonia, The Former Yugoslav Republic of", "Macedonia, Former", "FYROM"},
                  "RS": {"Kosovo", "Former Yugoslavia", "Former Serbia and Montenegro"},
                  # Kosovo currently mapped to Serbia for technical reasons because Kosovo is not currently its own 2 letter code in Debian or Pycountry (the dependencies of this library)
                  "SZ": {"Swaziland", "eswatini", "eSwatini"},
                  "LY": {"Libyan Arab Jamahiriya"},
                  "PS": {"Palestinian Territories, Occupied", "Palestinian Territory, occupied", "Palestine, Occupied",
                         "Occupied Palestine"},
                  "CN": {"Macau"},
                  "LC": {"St Lucia", "St. Lucia"},
                  "KN": {"St Kitts and Nevis", "St. Kitts and Nevis"},
                  "VC": {"St Vincent and the Grenadines", "St. Vincent and the Grenadines"},
                  # For compatibility with various versions of pycountry
                  "TR": {"Turkey", "Turkiye", "Türkiye"},
                  }
countries_maps = {}

def _add_variant(name: str, country):
    global countries_maps
    num_words = len(re.split(r" |-", name))
    if name == "the US":
        num_words = 1  # low prio
    if num_words not in countries_maps:
        countries_maps[num_words] = {}
    countries_map = countries_maps[num_words]
    no_spaces = re.sub(r" |-|'|\\|\.|,|\(|\)|\?", "", name)
    name = re.sub(" |-", "[- ]?", name)
    name = re.sub("'", "'?", name)
    name = re.sub(r"\(", "\\(", name)
    name = re.sub(r"\)", "\\)", name)
    name = re.sub(r"\.", "\\.", name)
    variants = {name, pycountry.remove_accents(name), pycountry.remove_accents(no_spaces)}
    for v in variants:
        if num_words == 1:
            countries_map[v] = country
            countries_map[v.upper()] = country
            countries_map[v.title()] = country
        else:
            countries_map[v.upper()] = country


def _add_variants(variants: list, alpha_2: str):
    country = pycountry.countries.lookup(alpha_2)
    for variant in variants:
        _add_variant(variant, country)


for country in pycountry.countries:
    _add_variant(country.name, country)
    clean_name = re.sub(r'( \(|,).+$', '', country.name)
    _add_variant(clean_name, country)
    _add_variant(re.sub(r"(?i)\band\b", "&", clean_name), country)

for alpha_2, variants in extra_synonyms.items():
    _add_variants(variants, alpha_2)


def _compile_regexes():
    # Create a set of regexes to be executed in order, from high to low accuracy.
    countries_regexes = []
    case_insensitive_regexes = []
    countries_master_map = {}
    for num_words, countries_map in sorted(countries_maps.items(), key=operator.itemgetter(0), reverse=True):
        countries_pattern = r"\b(" + "|".join(set(countries_map).difference({"US"})) + r")"
        if num_words <= 2:
            countries_pattern += r"\b"
        case_insensitive_regex = re.compile("(?i)" + countries_pattern)
        case_insensitive_regexes.append(case_insensitive_regex)
        if num_words > 1:
            countries_pattern = "(?i)" + countries_pattern
        countries_regex = re.compile(countries_pattern)
        countries_regexes.append(countries_regex)
        countries_master_map.update(countries_map)
    return countries_regexes, case_insensitive_regexes, countries_master_map


countries_regexes, case_insensitive_regexes, countries_master_map = _compile_regexes()


def add_custom_variants(variants: list, alpha_2: str):
    """
    Add a set of custom variant names for a country.
    :param variants: A list of strings e.g. ["Neverneverland", "Wonderland", "Disneyland"]
    :param alpha_2: the 2-letter country code in upper case e.g. "AE"
    """
    _add_variants(variants, alpha_2)
    global countries_regexes, case_insensitive_regexes, countries_master_map
    countries_regexes, case_insensitive_regexes, countries_master_map = _compile_regexes()


countries_exclusions = {"guinea[- ]*pig|canada[ -]*g(?:oo|ee)se"}
country_exclusion_pattern = r"(?i)(" + "|".join(countries_exclusions) + r")"
country_exclusion_regex = re.compile(country_exclusion_pattern)

# A set of key words which indicate Georgia the country if they occur within 3 tokens of a mention of Georgia
georgia_terms = {"country", "caucasus", "sakartvelo", "kartvelian", "ossetia", "black sea", "caspian", r"idze\b",
                 r"\btiflis\b",
                 r"adze\b",
                 r"vili\b",
                 'ს', 'ა', 'ქ', 'რ', 'თ', 'ვ', 'ე', 'ლ', 'ო',
                 r"\bBatumi\b",
                 r"\bKutaisi\b",
                 r"\bRustavi\b",
                 r"\bZugdidi\b",
                 r"\bKobuleti\b",
                 r"\bKhashuri\b",
                 r"\bSamtredia\b",
                 r"\bSenaki\b",
                 r"\bZestafoni\b",
                 r"\bMarneuli\b",
                 r"\bTelavi\b",
                 r"\bAkhaltsikhe\b",
                 r"\bOzurgeti\b",
                 r"\bKaspi\b",
                 r"\bChiatura\b",
                 r"\bTsqaltubo\b",
                 r"\bSagarejo\b",
                 r"\bGardabani\b",
                 r"\bBorjomi\b",
                 r"\bTkibuli\b",
                 r"\bKhoni\b",
                 r"\bBolnisi\b",
                 r"\bAkhalkalaki\b",
                 r"\bGurjaani\b",
                 r"\bMtskheta\b",
                 r"\bKvareli\b",
                 r"\bAkhmeta\b",
                 r"\bKareli\b",
                 r"\bLanchkhuti\b",
                 r"\bTsalenjikha\b",
                 r"\bDusheti\b",
                 r"\bSachkhere\b",
                 r"\bDedoplistsqaro\b",
                 r"\bLagodekhi\b",
                 r"\bNinotsminda\b",
                 r"\bAbasha\b",
                 r"\bTsnori\b",
                 r"\bTerjola\b",
                 r"\bMartvili\b",
                 r"\bJvari\b",
                 r"\bKhobi\b",
                 r"\bBaghdati\b",
                 r"\bTetritsqaro\b",
                 r"\bTsalka\b",
                 r"\bDmanisi\b",
                 r"\bAmbrolauri\b",
                 r"\bSighnaghi\b",
                 r"\bTsageri\b", }
for subd in pycountry.subdivisions:
    if subd.country_code == "GE":
        for word in re.split(r" |-", subd.name):
            georgia_terms.add(word)

georgia_pattern = r'(' + "|".join(georgia_terms) + r")"
georgia_regex_left = re.compile(
    f"(?i)({georgia_pattern}(\\w*\\W*)?(\\w*\\W*)?(\\w*\\W*)?(\\w*\\W*)?(\\w*\\W*)?(\\w*\\W*)?\\W*$)")
georgia_regex_right = re.compile(
    f"(?i)(^\\W*(\\w*\\W*)?(\\w*\\W*)?(\\w*\\W*)?(\\w*\\W*)?(\\w*\\W*)?(\\w*\\W*)?{georgia_pattern})")


def find_countries(text: str, is_ignore_case: bool = False, is_georgia_probably_the_country: bool = False) -> list:
    """
    Find all countries mentioned in the text.
    :param text: A string of text in English.
    :param is_ignore_case: Should case be ignored? By default the tool doesn't ignore case.
    :param is_georgia_probably_the_country: This option defaults to False. If we encounter the string "Georgia", is this probably the country in Eastern Europe? Most occurrences of Georgia in English text refer to the US state, so if your document is in a US-centric context it's best to leave this option set to False.
    :return: A list of tuples. Each tuple consists of a Pycountry country object, and a regex Match object.
    """
    country_matches_candidates = []

    exclusion_matches = list(country_exclusion_regex.finditer(text))
    is_excluded = set()
    for exclusion_match in exclusion_matches:
        for i in range(exclusion_match.start(), exclusion_match.end()):
            is_excluded.add(i)

    if is_ignore_case:
        regexes_to_use = case_insensitive_regexes
    else:
        regexes_to_use = countries_regexes
    for countries_regex in regexes_to_use:
        matches = countries_regex.finditer(text)
        for match in matches:
            if len(set(range(match.start(), match.end())).intersection(is_excluded)) > 0:
                continue

            normalised_name = pycountry.remove_accents(re.sub(r" |-|'|\\|\.|,|\(|\)", "", match.group().upper()))

            matched_country = countries_master_map[normalised_name]

            is_high_confidence = True
            if not is_georgia_probably_the_country and normalised_name == "GEORGIA":
                is_high_confidence = False

            country_matches_candidates.append((matched_country, match, is_high_confidence))

            for i in range(match.start(), match.end()):
                is_excluded.add(i)

    countries_found_set = set([c[0].alpha_2 for c in country_matches_candidates])

    sorted_candidate_matches = sorted(country_matches_candidates, key=lambda match: match[1].start())

    country_matches = []
    for matched_country, match, is_high_confidence in sorted_candidate_matches:
        is_include = True
        if matched_country.alpha_2 == "GE" and not is_high_confidence:
            is_include = False
            if len({"UA", "RO", "RU", "BY", "UZ", "KZ", "AR", "AZ", "TR", "MD"}.intersection(countries_found_set)) > 0:
                is_include = True
            else:
                left_context = text[:match.start()].strip()
                right_context = text[match.end():].strip()
                if georgia_regex_left.findall(left_context) or georgia_regex_right.findall(right_context):
                    is_include = True

        if is_include:
            country_matches.append((matched_country, match))

    return country_matches


