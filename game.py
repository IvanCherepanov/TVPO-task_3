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

class Game:
    def __init__(self, players):
        self.dict = CityRule()
        self.players = players
        self.kickedPlayers = []
        self.currentPlayer = 0
        self.lastChar = ''

    def check_move(self, city_name):
        #проверка наличия города в базе
        if self.dict.is_city(city_name):
            #проверка правильного начала\окончания города
            if self.lastChar == '' or self.lastChar == city_name[0].lower():
                #проверка назван ли был город
                if self.dict.is_available_city(city_name):
                    self.make_move(city_name)
                    self.dict.move_to_cache(city_name)
                    print('Корректно')
                    return 1
                else:
                    print('Город уже был назван')
                    return 2
            else:
                print('Неправильная буква')
                return 3
        else:
            print('Вы ввели не название русского города')
            return 4