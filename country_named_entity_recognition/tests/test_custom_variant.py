import unittest

from country_finder import add_custom_variants, find_countries


class TestCustomCountry(unittest.TestCase):

    def test_custom_country(self):
        add_custom_variants(["Neverneverland"], "AE")
        countries = find_countries("""I want to go to Neverneverland""")
        countries_found = set()
        for country, match in countries:
            countries_found.add(country.alpha_2)

        self.assertEqual({"AE"}, countries_found)
