import unittest

from country_finder import find_countries

north_american_alpha_2_codes = {'AG',
                                'AI',
                                'AW',
                                'BB',
                                'BL',
                                'BM',
                                'BQ',
                                'BS',
                                'BZ',
                                'CA',
                                'CR',
                                'CU',
                                'CW',
                                'DM',
                                'DO',
                                'GD',
                                'GL',
                                'GP',
                                'GT',
                                'HN',
                                'HT',
                                'JM',
                                'KN',
                                'KY',
                                'LC',
                                'MQ',
                                'MF',
                                'MS',
                                'MX',
                                'NI',
                                'PA',
                                'PM',
                                'PR',
                                'SV',
                                'SX',
                                'TC',
                                'TT',
                                'US',
                                'VC',
                                'VG',
                                'VI'}


class TestManyNorthAmericanCountriesAtOnce(unittest.TestCase):

    def test_all_countries_in_north_america(self):
        countries = find_countries("""ost visited North American countries the number one is the USA, where New York City is considered the most attractive landmark for travelers, further followed by Mexico and Canada.

The always up-to-date list of countries of North America in alphabetical order
A
Antigua and Barbuda
B
Bahamas
Barbados
Belize
C
Canada
Costa Rica
Cuba
D
Dominica
Dominican Republic
E
El Salvador
G
Grenada
Guatemala
H
Haiti
Honduras
J
Jamaica
M
Mexico
N
Nicaragua
P
Panama
S
Saint Kitts and Nevis
Saint Lucia
Saint Vincent and the Grenadines
T
Trinidad and Tobago
U
United States of America
List of dependent territories of North America in alphabetical order
A
Anguilla 
Aruba 
B
Bermuda 
Bonaire
British Virgin Islands 
C
Cayman Islands
Clipperton Island
Curacao
G
Greenland
Guadeloupe
M
Martinique 
Montserrat
N
Navassa Island
P
Puerto Rico
S
Saba
Saint Barthelemy
Saint Martin 
Saint Pierre and Miquelon 
Sint Eustatius 
Sint Maarten
T
Turks and Caicos Islands 
U
US Virgin Islands


 

""")

        countries_found = set()
        for country, match in countries:
            countries_found.add(country.alpha_2)

        self.assertEqual(north_american_alpha_2_codes, countries_found)
