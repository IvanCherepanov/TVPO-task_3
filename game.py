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

    #use or not use
    def is_available_city(self, city_name):
        return city_name not in self.cache_city

    def move_to_cache(self, city):
        # move to cache
        self.cache_city.add(city)
    
    def get_next_char(self, city_name):
        wrong_char = ("ъ", "ь", "ы", "й")
        city_name = city_name.lower()
        # get the next char/symbhol
        for char in city_name[::-1]:
            if char in wrong_char:
                continue
            else:
                break
        else:
            raise RuntimeError
        return char