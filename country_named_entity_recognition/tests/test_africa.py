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

african_alpha_2_codes = {'AO',
                         'BF',
                         'BI',
                         'BJ',
                         'BW',
                         'CD',
                         'CF',
                         'CG',
                         'CI',
                         'CM',
                         'CV',
                         'DJ',
                         'DZ',
                         'EG',
                         'ER',
                         'ET',
                         'GA',
                         'GH',
                         'GM',
                         'GN',
                         'GQ',
                         'GW',
                         'KE',
                         'KM',
                         'LR',
                         'LS',
                         'LY',
                         'MA',
                         'MG',
                         'ML',
                         'MR',
                         'MU',
                         'MW',
                         'MZ',
                         'NA',
                         'NE',
                         'NG',
                         'RW',
                         'SC',
                         'SD',
                         'SL',
                         'SN',
                         'SO',
                         'SS',
                         'ST',
                         'SZ',
                         'TD',
                         'TG',
                         'TN',
                         'TZ',
                         'UG',
                         'ZA',
                         'ZM',
                         'ZW'}


class TestManyAfricanCountriesAtOnce(unittest.TestCase):

    def test_all_countries_in_africa(self):
        countries = find_countries("""The always up-to-date list of countries of Africa in alphabetical order
        A
        Algeria
        Angola
        B
        Benin
        Botswana
        Burkina Faso
        Burundi
        C
        Cabo Verde
        Cameroon
        Central African Republic (CAR)
        Chad
        Comoros
        Congo, Democratic Republic of the
        Congo, Republic of the
        Cote d'Ivoire
        D
        Djibouti
        E
        Egypt
        Equatorial Guinea
        Eritrea
        Eswatini
        Ethiopia
        G
        Gabon
        Gambia
        Ghana
        Guinea
        Guinea-Bissau
        K
        Kenya
        L
        Lesotho
        Liberia
        Libya
        M
        Madagascar
        Malawi
        Mali
        Mauritania
        Mauritius
        Morocco
        Mozambique
        N
        Namibia
        Niger
        Nigeria
        R
        Rwanda
        S
        Sao Tome and Principe
        Senegal
        Seychelles
        Sierra Leone
        Somalia
        South Africa
        South Sudan
        Sudan
        T
        Tanzania
        Togo
        Tunisia
        U
        Uganda
        Z
        Zambia
        Zimbabwe and that's all""")

        countries_found = set()
        for country, match in countries:
            countries_found.add(country.alpha_2)

        self.assertEqual(african_alpha_2_codes, countries_found)
