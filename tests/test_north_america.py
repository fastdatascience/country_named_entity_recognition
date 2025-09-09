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

from country_named_entity_recognition.country_finder import find_countries

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



if __name__ == '__main__':
    unittest.main()