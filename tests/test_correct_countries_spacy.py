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

import unittest
import sys

sys.path.append("../src")
sys.path.append("../src/country_named_entity_recognition")

from country_named_entity_recognition.country_finder_spacy import find_countries_in_spacy_doc
import spacy

nlp = spacy.blank("en")

class TestFindCountriesSpacy(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual([], find_countries_in_spacy_doc(nlp, nlp("")))

    def test_no_matches(self):
        self.assertEqual([], find_countries_in_spacy_doc(nlp, nlp("the")))

    def test_one_country(self):
        countries = find_countries_in_spacy_doc(nlp, nlp("I went to Kenya."))
        self.assertEqual(1, len(countries))
        self.assertEqual("KE", countries[0][0].alpha_2)

    def test_ambiguity(self):
        countries = find_countries_in_spacy_doc(nlp, nlp("I went to Korea."))
        self.assertEqual(1, len(countries))
        self.assertEqual("KR", countries[0][0].alpha_2)

    def test_ambiguity_2(self):
        countries = find_countries_in_spacy_doc(nlp, nlp("I went to South Korea."))
        self.assertEqual(1, len(countries))
        self.assertEqual("KR", countries[0][0].alpha_2)

    def test_ambiguity_3(self):
        countries = find_countries_in_spacy_doc(nlp, nlp("I went to North Korea."))
        self.assertEqual(1, len(countries))
        self.assertEqual("KP", countries[0][0].alpha_2)

    def test_ambiguity_4(self):
        countries = find_countries_in_spacy_doc(nlp, nlp("I went to The Democratic People's Republic of Korea."))
        self.assertEqual(1, len(countries))
        self.assertEqual("KP", countries[0][0].alpha_2)

    def test_ambiguity_5(self):
        countries = find_countries_in_spacy_doc(nlp, nlp("I went to Guinea."))
        self.assertEqual(1, len(countries))
        self.assertEqual("GN", countries[0][0].alpha_2)

    def test_ambiguity_6(self):
        countries = find_countries_in_spacy_doc(nlp, nlp("I went to equatorial Guinea."))
        self.assertEqual(1, len(countries))
        self.assertEqual("GQ", countries[0][0].alpha_2)

    def test_ambiguity_7(self):
        countries = find_countries_in_spacy_doc(nlp, nlp("I have a Guinea pig."))
        self.assertEqual(0, len(countries))

    def test_english_name(self):
        countries = find_countries_in_spacy_doc(nlp, nlp("I went to the ivory coast"), is_ignore_case=True)
        self.assertEqual(1, len(countries))
        self.assertEqual("CI", countries[0][0].alpha_2)

    def test_name_no_accents(self):
        countries = find_countries_in_spacy_doc(nlp, nlp("I went to cote divoire"), is_ignore_case=True)
        self.assertEqual(1, len(countries))
        self.assertEqual("CI", countries[0][0].alpha_2)



if __name__ == '__main__':
    unittest.main()