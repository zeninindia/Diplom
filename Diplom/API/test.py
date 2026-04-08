import requests
from page_api import Apipage

api = Apipage()

def test_search_movies():
    name = 'я'
    response_body, status_code = api.search_movies1(name)  # распаковываем кортеж
    assert status_code == 200

    assert 'docs' in response_body
    docs = response_body['docs']

    first_movie = docs[0]

    assert 'Я' in first_movie['name']
    print(docs[0])

    assert first_movie['id'] == docs[0]['id']
    print(f"ID : {docs[0]['id']}")

    assert 'poster' in first_movie
    poster_url = first_movie['poster']
    print(f"Вот картинка фильма Я: {poster_url}")