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
                  "VG": {"British Virgin Islands"}, "SY": {"Syria"}, "GE": {"Republic of Georgia"},
                  'GM': {'gambia, republic of', 'gambia republic', 'republic of gambia', 'republic of the gambia'},
                  "NL": {"Nerlands"}, "IR": {"Iran"}
                  }
countries_maps = {}


def add_variant(name, country):
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


for country in pycountry.countries:
    add_variant(country.name, country)
    clean_name = re.sub(r'( \(|,).+$', '', country.name)
    add_variant(clean_name, country)
    add_variant(re.sub(r"(?i)\band\b", "&", clean_name), country)

for alpha_2, variants in extra_synonyms.items():
    country = pycountry.countries.lookup(alpha_2)
    for variant in variants:
        add_variant(variant, country)

# Create a set of regexes to be executed in order, from high to low accuracy.
countries_regexes = []
case_insensitive_regexes = []
countries_master_map = {}
for num_words, countries_map in sorted(countries_maps.items(), key=operator.itemgetter(0), reverse=True):
    countries_pattern = r"\b(" + "|".join(set(countries_map).difference({"US"})) + r")\b"
    case_insensitive_regex = re.compile("(?i)" + countries_pattern)
    case_insensitive_regexes.append(case_insensitive_regex)
    if num_words > 1:
        countries_pattern = "(?i)" + countries_pattern
    countries_regex = re.compile(countries_pattern)
    countries_regexes.append(countries_regex)
    countries_master_map.update(countries_map)

countries_exclusions = {"guinea[- ]*pig|canada[ -]*g(?:oo|ee)se"}
country_exclusion_pattern = r"(?i)(" + "|".join(countries_exclusions) + r")"
country_exclusion_regex = re.compile(country_exclusion_pattern)

# A set of key words which indicate Georgia the country if they occur within 3 tokens of a mention of Georgia
georgia_terms = {"country", "caucasus", "sakartvelo", "kartvelian", "ossetia", "black sea", "caspian", r"idze\b",
                 r"\btiflis\b",
                 r"adze\b",
                 r"shvili\b",
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
georgia_regex_left = re.compile(f"(?i)({georgia_pattern}(\\w*\\W*)?(\\w*\\W*)?(\\w*\\W*)?\\W*$)")
georgia_regex_right = re.compile(f"(?i)(^\\W*(\\w*\\W*)?(\\w*\\W*)?(\\w*\\W*)?{georgia_pattern})")


def find_countries(text: str, is_ignore_case: bool = False, is_georgia_probably_the_country: bool = False) -> str:
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

