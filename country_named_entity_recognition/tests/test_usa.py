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

from country_named_entity_recognition.country_finder import find_countries


class TestSynonymsForUSA(unittest.TestCase):

    def test_all_lower(self):
        countries = find_countries("I went to the us")
        self.assertEqual(0, len(countries))

    def test_ambiguity_case_insensitive(self):
        countries = find_countries("I went to the us", True)
        self.assertEqual(1, len(countries))
        self.assertEqual("US", countries[0][0].alpha_2)

    def test_name_with_dots(self):
        countries = find_countries("I went to the U.S.A.")
        self.assertEqual(1, len(countries))
        self.assertEqual("US", countries[0][0].alpha_2)

    def test_name_without_dots(self):
        countries = find_countries("born in the USA")
        self.assertEqual(1, len(countries))
        self.assertEqual("US", countries[0][0].alpha_2)

    def test_capital_us(self):
        countries = find_countries("TALKING ABOUT US AND")
        self.assertEqual(0, len(countries))

