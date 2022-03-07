import unittest

from countryfinder.country_finder import find_countries


class TestSynonymsForUSA(unittest.TestCase):

    def test_all_lower(self):
        countries = find_countries("I went to the us")
        self.assertEqual(0, len(countries))

    def test_ambiguity_case_insensitive(self):
        countries = find_countries("I went to the us", True)
        self.assertEqual(1, len(countries))
        self.assertEqual("US", countries[0][0].alpha_2)

    def test_name_with_dots(self):
        countries = find_countries("I went to the U.S.A.")
        self.assertEqual(1, len(countries))
        self.assertEqual("US", countries[0][0].alpha_2)

    def test_name_without_dots(self):
        countries = find_countries("born in the USA")
        self.assertEqual(1, len(countries))
        self.assertEqual("US", countries[0][0].alpha_2)

    def test_capital_us(self):
        countries = find_countries("TALKING ABOUT US AND")
        self.assertEqual(0, len(countries))

