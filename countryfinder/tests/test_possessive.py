import unittest

from countryfinder.country_finder import find_countries


class TestPossessive(unittest.TestCase):

    def test_simple_apostrophe(self):
        countries = find_countries("The UK's economy", True)
        self.assertEqual(1, len(countries))
        self.assertEqual("GB", countries[0][0].alpha_2)

    def test_simple_apostrophe_2(self):
        countries = find_countries("Britain's economy")
        self.assertEqual(1, len(countries))
        self.assertEqual("GB", countries[0][0].alpha_2)
