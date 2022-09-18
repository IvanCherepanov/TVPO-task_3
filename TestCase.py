import unittest
import os

from parsingCities import get_HTML_page, parse_to_file, normalize_cities
from game import CityRule

class ParsingTestCase(unittest.TestCase):
    def test_get_HTML_page(self):
        get_HTML_page()
        assert os.path.exists("data_base_cities.html") != False
        assert os.path.getsize("data_base_cities.html") > 0

    def test_parse_to_file(self):
        parse_to_file()
        assert os.path.exists("data_base_cities.html") != False
        assert os.path.getsize("data_base_cities.html") > 0

    def test_normalize_cities(self):
            assert normalize_cities("Москвёнок") == "москвенок"

class CityRuleTest(unittest.TestCase):
    
    def test_is_city(self):
        temp_temp = CityRule()
        assert temp_temp.is_city("Абакан") == True
        assert temp_temp.is_city("Абаканъ") != True