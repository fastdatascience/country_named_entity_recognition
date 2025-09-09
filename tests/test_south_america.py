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



if __name__ == '__main__':
    unittest.main()