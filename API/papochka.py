import requests
import json
import pytest

def test_search_movies():

    url = "https://api.poiskkino.dev/v1.4/movie/search"

    params = {
        'page': 1,
        'limit': 10,
        'query': 'я'
    }


    headers = {
        'accept': 'application/json',
        'X-API-KEY': 'GH99NQ5-Y6W49WP-QF0T6RT-FRH4YP9',
    }

    response = requests.get(url, params=params, headers=headers)

    response_json = response.json()
    print(response_json)

    assert response.status_code == 200

    assert 'docs' in response_json
    docs = response_json['docs']


    first_movie = docs[0]

    assert 'Я' in first_movie['name']
    print(docs[0])

    assert first_movie['id'] == docs[0]['id']
    print(f"ID : {docs[0]['id']}")

    assert 'poster' in first_movie
    poster_url = first_movie['poster']
    print(f"Вот картинка фильма Я: {poster_url}")


def test_search_genres_name():

    url = "https://api.poiskkino.dev/v1/movie/possible-values-by-field"

    headers = {
        'X-API-KEY': 'GH99NQ5-Y6W49WP-QF0T6RT-FRH4YP9'
    }

    params = {
        'field': 'genres.name'
    }



    response = requests.get(url, headers=headers, params=params, timeout=10)
    response_json = response.json()
    print(response_json)
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

    film_poster = list['poster']
    assert 'poster' in list
    assert film_poster is not None
    assert 'url' in film_poster
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

    print("Список Имен:")
    for name in en_names:
        print(f"- {name}")