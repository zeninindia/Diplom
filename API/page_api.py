import selenium
import pytest
import requests
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import allure
import selenium
import pytest
from selenium import webdriver
# сюда нужно импортировать класс, и тогда фикстуры заработают
from selenium.webdriver.chrome.options import Options


class Apipage:
    def __init__(self):
        self.url = "https://api.poiskkino.dev/"
        self.key = 'GH99NQ5-Y6W49WP-QF0T6RT-FRH4YP9'


    def search_movies1(self, name):
        pen = f"{self.url}v1.4/movie/search"
        params = {
            'page': 1,
            'limit': 10,
            'query': name
        }

        headers = {
            'accept': 'application/json',
            'X-API-KEY': self.key
        }

        response = requests.get(pen, params=params, headers=headers)
        response_body = response.json()
        status_code = response.status_code
        return response_body, status_code

def test_search_genres_name():

    url = "https://api.poiskkino.dev/v1/movie/possible-values-by-field"

    headers = {
        'X-API-KEY': 'GH99NQ5-Y6W49WP-QF0T6RT-FRH4YP9'
    }

    params = {
        'field': 'genres.name'
    }



    response = requests.get(url, headers=headers, params=params)
    response_json = response.json()
    print(response_json)
    print("\n=== ОТЛАДКА ===")
    print(f"Статус ответа: {response.status_code}")
    print(f"Заголовки ответа: {dict(response.headers)}")
    print(f"Тип контента: {response.headers.get('content-type', 'не указан')}")
    print(f"Тело ответа (первые 500 символов):\n{response.text[:500]}")
    print("=== КОНЕЦ ОТЛАДКИ ===")
    assert response.status_code == 200
    print("Yupeee it works")

    items = response_json

    print(len(items))


    for item in items:
        print(item['name'])



    first_name = items[0]['name']
    print(f"Имя первого элемента: {first_name}")
    first_slug = items[0]['slug']
    print(f"Slug первого элемента: {first_slug}")

    second_name = items[1]['name']
    print(f"Slug второго элемента: {second_name}")
    second_slug = items[1]['slug']
    print(f"Slug второго элемента: {second_slug}")
    print("И даже это напечатал, УРААА")



def test_search_random():

    url = "https://api.poiskkino.dev/v1.4/movie/random"

    headers = {
        'X-API-KEY': 'GH99NQ5-Y6W49WP-QF0T6RT-FRH4YP9'
    }

    response = requests.get(url, headers=headers)
    print(response.text)
    assert response.status_code == 200

    list = response.json()
    movie_name = list['alternativeName']
    print(movie_name)

    film_poster = list["poster"]
    assert "poster" in list
    assert film_poster is not None
    assert "url" in film_poster
    poster_url = film_poster
    print(poster_url)


def test_search_nominations():
    url = "https://api.poiskkino.dev/v1.4/movie/awards"

    headers = {
        'X-API-KEY': 'GH99NQ5-Y6W49WP-QF0T6RT-FRH4YP9'
    }

    response = requests.get(url, headers=headers)
    print(response.text)
    assert response.status_code == 200

    response_json = response.json()
    assert 'docs' in response_json
    docs = response_json['docs']
    assert len(docs) > 0

    for doc in docs:
        nomination = doc['nomination']
        assert (nomination, list)
        award = nomination['award']
        assert (award, list)



def test_search_names():

    url = "https://api.poiskkino.dev/v1.4/person/search"


    headers = {
        'X-API-KEY': 'GH99NQ5-Y6W49WP-QF0T6RT-FRH4YP9'
    }

    response = requests.get(url, headers=headers)
    print(response.text)
    assert response.status_code == 200

    response_body = response.json()

    assert 'docs' in response_body
    persons = response_body['docs']
    assert len(persons) > 0

    assert 'total' in response_body
    total_count = response_body['total']
    assert total_count > 0
    en_names = []
    for person in persons:
        assert 'enName' in person
        en_name = person['enName']
        en_names.append(en_name)

    print("Список имен:")
    for name in en_names:
        print(f"- {name}")



    def search_movies(self,  name):
        name = 'я'
        url = "https://api.poiskkino.dev/v1.4/movie/search"
        params = {
            'page': 1,
            'limit': 10,
            'query': name
        }
        headers = {
            'X-API-KEY': 'GH99NQ5-Y6W49WP-QF0T6RT-FRH4YP9'
        }
        response = requests.get(url, params=params, headers=headers)
        response_json = response.json()

        return(response_json)