import unittest

from country_finder import find_countries

european_alpha_2_codes = {'AD',
                          'AL',
                          'AT',
                          'BA',
                          'BE',
                          'BG',
                          'BY',
                          'CH',
                          'CZ',
                          'DE',
                          'DK',
                          'EE',
                          'ES',
                          'FI',
                          'FR',
                          'GB',
                          'GR',
                          'HR',
                          'HU',
                          'IE',
                          'IS',
                          'IT',
                          'LI',
                          'LT',
                          'LU',
                          'LV',
                          'MC',
                          'MD',
                          'ME',
                          'MK',
                          'MT',
                          'NL',
                          'NO',
                          'PL',
                          'PT',
                          'RO',
                          'RS',
                          'RU',
                          'SE',
                          'SI',
                          'SK',
                          'SM',
                          'UA',
                          'VA'}


class TestManyEuropeanCountriesAtOnce(unittest.TestCase):

    def test_all_countries_in_europe(self):
        countries = find_countries("""w, with current population and subregion (based on the United Nations official statistics).

Not included in this total of "countries" and listed separately are:

Dependencies (or dependent territories, dependent areas) or Areas of Special Sovereignty (autonomous territories)
Search:
#	Country	Population
(2020)	Subregion
1	Russia	145,934,462	Eastern Europe
2	Germany	83,783,942	Western Europe
3	United Kingdom	67,886,011	Northern Europe
4	France	65,273,511	Western Europe
5	Italy	60,461,826	Southern Europe
6	Spain	46,754,778	Southern Europe
7	Ukraine	43,733,762	Eastern Europe
8	Poland	37,846,611	Eastern Europe
9	Romania	19,237,691	Eastern Europe
10	Netherlands	17,134,872	Western Europe
11	Belgium	11,589,623	Western Europe
12	Czech Republic (Czechia)	10,708,981	Eastern Europe
13	Greece	10,423,054	Southern Europe
14	Portugal	10,196,709	Southern Europe
15	Sweden	10,099,265	Northern Europe
16	Hungary	9,660,351	Eastern Europe
17	Belarus	9,449,323	Eastern Europe
18	Austria	9,006,398	Western Europe
19	Serbia	8,737,371	Southern Europe
20	Switzerland	8,654,622	Western Europe
21	Bulgaria	6,948,445	Eastern Europe
22	Denmark	5,792,202	Northern Europe
23	Finland	5,540,720	Northern Europe
24	Slovakia	5,459,642	Eastern Europe
25	Norway	5,421,241	Northern Europe
26	Ireland	4,937,786	Northern Europe
27	Croatia	4,105,267	Southern Europe
28	Moldova	4,033,963	Eastern Europe
29	Bosnia and Herzegovina	3,280,819	Southern Europe
30	Albania	2,877,797	Southern Europe
31	Lithuania	2,722,289	Northern Europe
32	North Macedonia	2,083,374	Southern Europe
33	Slovenia	2,078,938	Southern Europe
34	Latvia	1,886,198	Northern Europe
35	Estonia	1,326,535	Northern Europe
36	Montenegro	628,066	Southern Europe
37	Luxembourg	625,978	Western Europe
38	Malta	441,543	Southern Europe
39	Iceland	341,243	Northern Europe
40	Andorra	77,265	Southern Europe
41	Monaco	39,242	Western Europe
42	Liechtenstein	38,128	Western Europe
43	San Marino	33,931	Southern Europe
44	Holy See	801	Southern Europe
Dependencies or other territories
""")

        countries_found = set()
        for country, match in countries:
            countries_found.add(country.alpha_2)

        self.assertEqual(european_alpha_2_codes, countries_found)
