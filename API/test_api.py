import requests
import pytest

def test_search_movies():
    """Выполняет поиск фильмов с фиксированными параметрами."""
    url = "https://api.poiskkino.dev/v1.4/movie/search?page=1&limit=10&query=я"

    payload = "{\"query\":\"\",\"variables\":{}}"

    headers = {
        'accept': 'application/json',
        'X-API-KEY': 'GH99NQ5-Y6W49WP-QF0T6RT-FRH4YP9',
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    response_json = response.json()
    assert response.status_code == 200
    assert 'docs' in response_json, "Response does not contain 'docs' key"

    docs = response_json['docs']

    # Проверяем, что docs — список и содержит от 1 до 10 элементов (по limit=10)
    assert isinstance(docs, list), "'docs' is not a list"

def test_search_1():
    """Выполняет поиск фильмов с фиксированными параметрами."""
    #url = "https://api.poiskkino.dev/v1.4/movie/search?page=1&limit=10&query=я"
    url = "https://api.poiskkino.dev/v1/movie/possible-values-by-field?field=genres.name"

    payload = "{}"

    headers = {
        'X-API-KEY': 'GH99NQ5-Y6W49WP-QF0T6RT-FRH4YP9'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200


def test_search_2():
    """Выполняет поиск фильмов с фиксированными параметрами."""
    url = "https://api.poiskkino.dev/v1.4/movie/random"
    # url = "https://api.poiskkino.dev/v1/movie/possible-values-by-field?field=genres.name"

    payload = "{}"

    headers = {
        'X-API-KEY': 'GH99NQ5-Y6W49WP-QF0T6RT-FRH4YP9'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200


def test_search_3():
    """Выполняет поиск фильмов с фиксированными параметрами."""
    url = "https://api.poiskkino.dev/v1.4/movie/awards"
    # url = "https://api.poiskkino.dev/v1/movie/possible-values-by-field?field=genres.name"

    payload = "{}"

    headers = {
        'X-API-KEY': 'GH99NQ5-Y6W49WP-QF0T6RT-FRH4YP9'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200

def test_search_4():
    """Выполняет поиск фильмов с фиксированными параметрами."""
    # url = "https://api.poiskkino.dev/v1.4/movie/awards"
    # url = "https://api.poiskkino.dev/v1/movie/possible-values-by-field?field=genres.name"
    url = "https://api.poiskkino.dev/v1.4/person/search?page=1&limit=10&query="

    payload = "{}"

    headers = {
        'X-API-KEY': 'GH99NQ5-Y6W49WP-QF0T6RT-FRH4YP9'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200
