from locale import normalize
from parsingCities import get_HTML_page, normalize_cities, parse_to_file

class CityRule:
    def __init__(self):
        self.cache_city = set()
        self.cities = {}
        with open("cities.txt", "r", encoding="utf-8") as f:
            self.cities = {normalize_cities(x) for x in f.readlines() if x.strip()}#strip - delete spaces

    def is_city(self, city_name):
        
        city_name = normalize_cities(city_name)
        return city_name in self.cities