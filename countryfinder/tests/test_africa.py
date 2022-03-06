import unittest

from countryfinder.country_finder import find_countries

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
