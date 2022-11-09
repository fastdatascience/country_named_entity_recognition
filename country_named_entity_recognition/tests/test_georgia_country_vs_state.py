import unittest

from country_finder import find_countries


class TestSynonymsForUSA(unittest.TestCase):

    def test_american_address(self):
        countries = find_countries("8757 Georgia Avenue, 12th Floor")
        self.assertEqual(0, len(countries))

    def test_other_eastern_european_countries(self):
        countries = find_countries("countries including Poland, Hungary, Czech republic, Slovakia, Georgia, Russia, Ukraine, Bulgaria and Latvia", True)
        self.assertEqual(9, len(countries))
        self.assertEqual("PL", countries[0][0].alpha_2)
        self.assertEqual("HU", countries[1][0].alpha_2)
        self.assertEqual("CZ", countries[2][0].alpha_2)
        self.assertEqual("SK", countries[3][0].alpha_2)
        self.assertEqual("GE", countries[4][0].alpha_2)
        self.assertEqual("RU", countries[5][0].alpha_2)
        self.assertEqual("UA", countries[6][0].alpha_2)
        self.assertEqual("BG", countries[7][0].alpha_2)
        self.assertEqual("LV", countries[8][0].alpha_2)

    def test_georgian_address(self):
        countries = find_countries("""2. Dr. Avtandil Abramashvili
Kristine Sharashidze Street #19
Tbilisi, Georgia 0131""")
        self.assertEqual(1, len(countries))
        self.assertEqual("GE", countries[0][0].alpha_2)

    def test_georgia_country(self):
        countries = find_countries("Georgia (საქართველო, Sakartvelo; IPA: [sɑkʰɑrtʰvɛlɔ]), officially the Republic of Georgia from 1990 to 1995,")
        self.assertEqual(2, len(countries))
        self.assertEqual("GE", countries[0][0].alpha_2)
        self.assertEqual("GE", countries[1][0].alpha_2)

    def test_georgia_state(self):
        countries = find_countries("Georgia is a state in the Southeastern region of the United States, bordered to the north by Tennessee and North Carolina")
        self.assertEqual(1, len(countries))
        self.assertEqual("US", countries[0][0].alpha_2)

