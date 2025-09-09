import pycountry
import re
import spacy
from spacy.matcher import PhraseMatcher
from country_named_entity_recognition.common import extra_synonyms

# A set of key words which indicate Georgia the country if they occur within 3 tokens of a mention of Georgia
georgia_country_terms = {"country", "caucasus", "sakartvelo", "kartvelian", "ossetia", "black sea", "caspian", "idze",
                         "tiflis",
                         "batumi",
                         "kutaisi",
                         "rustavi",
                         "zugdidi",
                         "kobuleti",
                         "khashuri",
                         "samtredia",
                         "senaki",
                         "zestafoni",
                         "marneuli",
                         "telavi",
                         "akhaltsikhe",
                         "ozurgeti",
                         "kaspi",
                         "chiatura",
                         "tsqaltubo",
                         "sagarejo",
                         "gardabani",
                         "borjomi",
                         "tkibuli",
                         "khoni",
                         "bolnisi",
                         "akhalkalaki",
                         "gurjaani",
                         "mtskheta",
                         "kvareli",
                         "akhmeta",
                         "kareli",
                         "lanchkhuti",
                         "tsalenjikha",
                         "dusheti",
                         "sachkhere",
                         "dedoplistsqaro",
                         "lagodekhi",
                         "ninotsminda",
                         "abasha",
                         "tsnori",
                         "terjola",
                         "martvili",
                         "jvari",
                         "khobi",
                         "baghdati",
                         "tetritsqaro",
                         "tsalka",
                         "dmanisi",
                         "ambrolauri",
                         "sighnaghi",
                         "tsageri"}

patterns = {}

alpha_2_to_obj = {}
for country in pycountry.countries:
    alpha_2_to_obj[country.alpha_2] = country
    if country.alpha_2 not in patterns:
        patterns[country.alpha_2] = []

    variants = set()
    variants.add(country.name)
    clean_name = re.sub(r'( \(|,).+$', '', country.name)
    variants.add(clean_name)
    variants.add(re.sub(r"(?i)\band\b", "&", clean_name))
    patterns[country.alpha_2].extend(list(variants))

for country_code, synonyms in extra_synonyms.items():
    if country_code not in patterns:
        patterns[country_code] = []
    for name in synonyms:
        if name not in patterns[country_code]:
            patterns[country_code].append(name)


def init_phrase_matcher(nlp):
    phrase_matcher = PhraseMatcher(nlp.vocab)
    phrase_matcher_lower_case = PhraseMatcher(nlp.vocab, attr="LOWER")
    phrase_matcher_georgia = PhraseMatcher(nlp.vocab, attr="LOWER")
    phrase_matcher_exclusion = PhraseMatcher(nlp.vocab, attr="LOWER")

    for pattern_name, pattern_surface_forms in patterns.items():
        phrase_matcher.add(pattern_name, nlp.pipe(pattern_surface_forms))

    for pattern_name, pattern_surface_forms in patterns.items():
        phrase_matcher_lower_case.add(pattern_name, nlp.pipe([x.lower() for x in pattern_surface_forms]))

    phrase_matcher_georgia.add("georgia", nlp.pipe(georgia_country_terms))
    phrase_matcher_exclusion.add("exclusion", nlp.pipe(["guinea pig", "guinea pigs", "canada goose", "canada geese"]))

    return phrase_matcher, phrase_matcher_lower_case, phrase_matcher_georgia, phrase_matcher_exclusion

phrase_matcher_holder = {}

def find_countries_in_spacy_doc(nlp: spacy.language.Language, doc: spacy.tokens.doc.Doc, is_ignore_case=False, is_georgia_probably_the_country: bool = False):
    if id(nlp) not in phrase_matcher_holder:
        phrase_matcher_holder[id(nlp)] = init_phrase_matcher(nlp)

    phrase_matcher, phrase_matcher_lower_case, phrase_matcher_georgia, phrase_matcher_exclusion = phrase_matcher_holder[id(nlp)]

    country_matches = []

    if is_ignore_case:
        matches = list(phrase_matcher_lower_case(doc))
    else:
        matches = list(phrase_matcher(doc))

    georgia_indices = set()
    if not is_georgia_probably_the_country:
        georgia_matches = list(phrase_matcher_georgia(doc))
        for match in georgia_matches:
            georgia_indices.add(match[1])
            georgia_indices.add(match[2])

    matches = sorted(matches, key=lambda match: match[2] - match[1], reverse=True)

    tokens_already_used = set()

    exclusion_matches = list(phrase_matcher_exclusion(doc))
    for match in exclusion_matches:
        for idx in range(match[1], match[2]):
            tokens_already_used.add(idx)

    for phrase_match in matches:
        is_already_used = False
        for idx in range(phrase_match[1], phrase_match[2]):
            if idx in tokens_already_used:
                is_already_used = True

        if is_already_used:
            continue
        matched_country = nlp.vocab.strings[phrase_match[0]]
        if matched_country == "GE" and not is_georgia_probably_the_country:
            start_idx = phrase_match[1]
            end_idx = phrase_match[2]
            dist = 999999
            for test_idx in georgia_indices:
                dist1 = abs(test_idx - start_idx)
                dist2 = abs(test_idx - end_idx)
                dist = min([dist, dist1, dist2])
            if dist > 3:
                continue

        country_matches.append((alpha_2_to_obj[matched_country], phrase_match))

        for idx in range(phrase_match[1], phrase_match[2]):
            tokens_already_used.add(idx)

    return country_matches


if __name__ == "__main__":
    nlp = spacy.blank("en")
    doc = nlp("Born in the USA")
    print (find_countries_in_spacy_doc(nlp, doc))