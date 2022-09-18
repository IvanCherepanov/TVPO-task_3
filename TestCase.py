import unittest
import os

class ParsingTestCase(unittest.TestCase):
    def test_get_HTML_page(self):
        get_HTML_page()
        assert os.path.exists("data_base_cities.html") != False
        assert os.path.getsize("data_base_cities.html") > 0