'''
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

'''

import unittest

from country_finder import find_countries

oceanian_alpha_2_codes ={'AS',
 'AU',
 'CK',
 'FJ',
 'FM',
 'GU',
 'KI',
 'MH',
 'MP',
 'NC',
 'NR',
 'NU',
 'NZ',
 'PF',
 'PG',
 'PW',
 'SB',
 'TK',
 'TO',
 'TV',
 'VU',
 'WF',
 'WS'}


class TestManyOceanianCountriesAtOnce(unittest.TestCase):

    def test_all_countries_in_oceania(self):
        countries = find_countries("""Search:
#	Country	Population
(2020)	Subregion
1	Australia	25,499,884	Australia and New Zealand
2	Papua New Guinea	8,947,024	Melanesia
3	New Zealand	4,822,233	Australia and New Zealand
4	Fiji	896,445	Melanesia
5	Solomon Islands	686,884	Melanesia
6	Micronesia	548,914	Micronesia
7	Vanuatu	307,145	Melanesia
8	Samoa	198,414	Polynesia
9	Kiribati	119,449	Micronesia
10	Tonga	105,695	Polynesia
11	Marshall Islands	59,190	Micronesia
12	Palau	18,094	Micronesia
13	Tuvalu	11,792	Polynesia
14	Nauru	10,824	Micronesia
cies or other territories
#	Territory	Population
(2020)	Dependency of
1	New Caledonia	285,498	
2	French Polynesia	280,908	
3	Guam	168,775	
4	Northern Mariana Islands	57,559
5	American Samoa	55,19
6	Cook Islands	17,564
7	Wallis & Futuna	11,239	
8	Niue	1,626
9	Tokelau	1,357	
""")

        countries_found = set()
        for country, match in countries:
            countries_found.add(country.alpha_2)

        self.assertEqual(oceanian_alpha_2_codes, countries_found)
