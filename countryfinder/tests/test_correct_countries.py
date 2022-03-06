import unittest

from countryfinder.country_finder import find_countries


class TestFindCountries(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual([], find_countries(""))

    def test_no_matches(self):
        self.assertEqual([], find_countries("the"))

    def test_one_country(self):
        countries = find_countries("I went to Kenya.")
        self.assertEqual(1, len(countries))
        self.assertEqual("KE", countries[0][0].alpha_2)

    def test_ambiguity(self):
        countries = find_countries("I went to Korea.")
        self.assertEqual(1, len(countries))
        self.assertEqual("KR", countries[0][0].alpha_2)

    def test_ambiguity_2(self):
        countries = find_countries("I went to South Korea.")
        self.assertEqual(1, len(countries))
        self.assertEqual("KR", countries[0][0].alpha_2)

    def test_ambiguity_3(self):
        countries = find_countries("I went to North Korea.")
        self.assertEqual(1, len(countries))
        self.assertEqual("KP", countries[0][0].alpha_2)

    def test_ambiguity_4(self):
        countries = find_countries("I went to The Democratic People's Republic of Korea.")
        self.assertEqual(1, len(countries))
        self.assertEqual("KP", countries[0][0].alpha_2)

    def test_ambiguity_5(self):
        countries = find_countries("I went to Guinea.")
        self.assertEqual(1, len(countries))
        self.assertEqual("GN", countries[0][0].alpha_2)

    def test_ambiguity_6(self):
        countries = find_countries("I went to equatorial Guinea.")
        self.assertEqual(1, len(countries))
        self.assertEqual("GQ", countries[0][0].alpha_2)

    def test_ambiguity_7(self):
        countries = find_countries("I have a Guinea pig.")
        self.assertEqual(0, len(countries))

    def test_ambiguity_8(self):
        countries = find_countries("I went to the us")
        self.assertEqual(0, len(countries))

    def test_ambiguity_case_insensitive(self):
        countries = find_countries("I went to the us", True)
        self.assertEqual(1, len(countries))
        self.assertEqual("US", countries[0][0].alpha_2)

    def test_english_name(self):
        countries = find_countries("I went to the ivory coast")
        self.assertEqual(1, len(countries))
        self.assertEqual("CI", countries[0][0].alpha_2)

    def test_name_no_accents(self):
        countries = find_countries("I went to cote divoire")
        self.assertEqual(1, len(countries))
        self.assertEqual("CI", countries[0][0].alpha_2)

    def test_name_with_dots(self):
        countries = find_countries("I went to the U.S.A.")
        self.assertEqual(1, len(countries))
        self.assertEqual("US", countries[0][0].alpha_2)

    def test_name_without_dots(self):
        countries = find_countries("born in the USA")
        self.assertEqual(1, len(countries))
        self.assertEqual("US", countries[0][0].alpha_2)
