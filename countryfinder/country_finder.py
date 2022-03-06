import operator
import re

import pycountry

extra_synonyms = {"VN": {"Vietnam"}, "US": {"USA", "the US", r"U\.S", r"U\.S\."}, "CZ": {"Czech Rep", "Czech Republic"},
                  "AE": {"UAE", r"U\.A\.E\."},
                  "KR": {"Korea", "Republic of Korea"}, "KP": {"North Korea", "Democratic People's Republic of Korea"},
                  "CI": {"Ivory Coast"}, "CD": {"Congo, Democratic Republic", "Democratic Republic of the Congo",
                                                "Democratic Republic of Congo", "DR Congo", "DRC"},
                  "CV": {"Cape Verde"}, "SH": {r"St\.? Helena"},
                  "GB": {"Britain", "United Kingdom", "UK", r"U\.K", r"U\.K\."},
                  "RU": {"Russia"}, "VA": {"Holy See"}, "BN": {"Brunei"}, "LA": {"Laos"},
                  "VG": {"British Virgin Islands"}, "SY": {"Syria"}
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


def find_countries(text: str, is_ignore_case: bool = False) -> str:
    country_matches = []

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

            country_matches.append((matched_country, match))

            for i in range(match.start(), match.end()):
                is_excluded.add(i)

    return sorted(country_matches, key=lambda match: match[1].start())
