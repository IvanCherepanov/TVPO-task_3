import requests
from bs4 import BeautifulSoup

def get_HTML_page():
    URL = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8"

    r = requests.get(URL)
    with open("data_base_cities.html", "w", encoding="utf-8") as f:
        f.write(r.text)
