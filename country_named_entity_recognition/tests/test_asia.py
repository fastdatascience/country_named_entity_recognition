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

asian_alpha_2_codes = {'AE',
                       'AF',
                       'AM',
                       'AZ',
                       'BD',
                       'BH',
                       'BN',
                       'BT',
                       'CN',
                       'CY',
                       'GE',
                       'HK',
                       'ID',
                       'IL',
                       'IN',
                       'IQ',
                       'IR',
                       'JO',
                       'JP',
                       'KG',
                       'KH',
                       'KP',
                       'KR',
                       'KW',
                       'KZ',
                       'LA',
                       'LB',
                       'LK',
                       'MM',
                       'MN',
                       'MO',
                       'MV',
                       'MY',
                       'NP',
                       'OM',
                       'PH',
                       'PK',
                       'PS',
                       'QA',
                       'SA',
                       'SG',
                       'SY',
                       'TH',
                       'TJ',
                       'TL',
                       'TM',
                       'TR',
                       'TW',
                       'UZ',
                       'VN',
                       'YE'}


class TestManyAsianCountriesAtOnce(unittest.TestCase):

    def test_all_countries_in_asia(self):
        countries = find_countries("""omous territories)
Search:
#	Country	Population
(2020)	Subregion
1	China	1,439,323,776	Eastern Asia
2	India	1,380,004,385	Southern Asia
3	Indonesia	273,523,615	South-Eastern Asia
4	Pakistan	220,892,340	Southern Asia
5	Bangladesh	164,689,383	Southern Asia
6	Japan	126,476,461	Eastern Asia
7	Philippines	109,581,078	South-Eastern Asia
8	Vietnam	97,338,579	South-Eastern Asia
9	Turkey	84,339,067	Western Asia
10	Iran	83,992,949	Southern Asia
11	Thailand	69,799,978	South-Eastern Asia
12	Myanmar	54,409,800	South-Eastern Asia
13	South Korea	51,269,185	Eastern Asia
14	Iraq	40,222,493	Western Asia
15	Afghanistan	38,928,346	Southern Asia
16	Saudi Arabia	34,813,871	Western Asia
17	Uzbekistan	33,469,203	Central Asia
18	Malaysia	32,365,999	South-Eastern Asia
19	Yemen	29,825,964	Western Asia
20	Nepal	29,136,808	Southern Asia
21	North Korea	25,778,816	Eastern Asia
22	Sri Lanka	21,413,249	Southern Asia
23	Kazakhstan	18,776,707	Central Asia
24	Syria	17,500,658	Western Asia
25	Cambodia	16,718,965	South-Eastern Asia
26	Jordan	10,203,134	Western Asia
27	Azerbaijan	10,139,177	Western Asia
28	United Arab Emirates	9,890,402	Western Asia
29	Tajikistan	9,537,645	Central Asia
30	Israel	8,655,535	Western Asia
31	Laos	7,275,560	South-Eastern Asia
32	Lebanon	6,825,445	Western Asia
33	Kyrgyzstan	6,524,195	Central Asia
34	Turkmenistan	6,031,200	Central Asia
35	Singapore	5,850,342	South-Eastern Asia
36	Oman	5,106,626	Western Asia
37	State of Palestine	5,101,414	Western Asia
38	Kuwait	4,270,571	Western Asia
39	Georgia	3,989,167	Western Asia
40	Mongolia	3,278,290	Eastern Asia
41	Armenia	2,963,243	Western Asia
42	Qatar	2,881,053	Western Asia
43	Bahrain	1,701,575	Western Asia
44	Timor-Leste	1,318,445	South-Eastern Asia
45	Cyprus	1,207,359	Western Asia
46	Bhutan	771,608	Southern Asia
47	Maldives	540,544	Southern Asia
48	Brunei	437,479	South-Eastern Asia
Dependencies or other territories
#	Territory	Population
(2020)	Dependency of
1	Taiwan	23,816,775	(China)
2	Hong Kong	7,496,981	China
3	Macao	649,335	China
""")

        countries_found = set()
        for country, match in countries:
            countries_found.add(country.alpha_2)

        self.assertEqual(asian_alpha_2_codes, countries_found)
