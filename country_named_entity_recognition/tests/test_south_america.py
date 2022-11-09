import unittest

from country_finder import find_countries

south_american_alpha_2_codes = {'AR',
                                'BO',
                                'BR',
                                'CL',
                                'CO',
                                'EC',
                                'FK',
                                'GF',
                                'GS',
                                'GY',
                                'PE',
                                'PY',
                                'SR',
                                'UY',
                                'VE'}


class TestManySouthAmericanCountriesAtOnce(unittest.TestCase):

    def test_all_countries_in_europe(self):
        countries = find_countries("""ng the South American countries are Brazil, Argentina, and Peru, the last one is the home of the region's most famous tourist attraction Machu Picchu, the mysterious city of the Incas.

The always up-to-date list of countries of South America in alphabetical order
A
Argentina
B
Bolivia
Brazil
C
Chile
Colombia
E
Ecuador
G
Guyana
P
Paraguay
Peru
S
Suriname
U
Uruguay
V
Venezuela
List of dependent territories of South America in alphabetical order
F
Falkland Islands 
French Guiana 
S
South Georgia and the South Sandwich Islands 
""")

        countries_found = set()
        for country, match in countries:
            countries_found.add(country.alpha_2)

        self.assertEqual(south_american_alpha_2_codes, countries_found)
