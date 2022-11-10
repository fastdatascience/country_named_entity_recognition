import unittest

from country_finder import find_countries


class TestSynonymsForVirginIslands(unittest.TestCase):

    def test_us_vi(self):
        countries = find_countries("Holiday in Virgin Islands (U.S.)")
        print(countries)
        self.assertEqual(1, len(countries))
        self.assertEqual("VI", countries[0][0].alpha_2)

    def test_british_vi(self):
        countries = find_countries("Holiday in Virgin Islands (British)")
        print(countries)
        self.assertEqual(1, len(countries))
        self.assertEqual("VG", countries[0][0].alpha_2)
