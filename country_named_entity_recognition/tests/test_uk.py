import unittest

from countryfinder.country_finder import find_countries


class TestSynonymsForUSA(unittest.TestCase):

    def test_all_lower(self):
        countries = find_countries("I went to the uk")
        self.assertEqual(0, len(countries))

    def test_ambiguity_case_insensitive(self):
        countries = find_countries("I went to the uk", True)
        self.assertEqual(1, len(countries))
        self.assertEqual("GB", countries[0][0].alpha_2)

    def test_name_with_dots(self):
        countries = find_countries("I went to the U.K.")
        self.assertEqual(1, len(countries))
        self.assertEqual("GB", countries[0][0].alpha_2)

    def test_name_without_dots(self):
        countries = find_countries("born in the UK")
        self.assertEqual(1, len(countries))
        self.assertEqual("GB", countries[0][0].alpha_2)

    def test_capital_uk(self):
        countries = find_countries("TALKING ABOUT UK AND")
        self.assertEqual(1, len(countries))
        self.assertEqual("GB", countries[0][0].alpha_2)

    def test_britain(self):
        countries = find_countries("I went to Britain")
        self.assertEqual(1, len(countries))
        self.assertEqual("GB", countries[0][0].alpha_2)

    def test_united_kingdom_lowercase(self):
        countries = find_countries("I went to the united kingdom")
        self.assertEqual(1, len(countries))
        self.assertEqual("GB", countries[0][0].alpha_2)
