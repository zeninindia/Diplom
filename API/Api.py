import requests
import json
import pytest
import allure
from selenium import webdriver
from page_api import Apipage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os

load_dotenv()


class ApiClass:
    def __init__(self, url: str) -> None:
        self.url = url or os.getenv("URL")
        self.headers = {
            "accept": "application/json",
            "X-API-KEY": os.getenv("X_API_KEY")
        }

    def search_movies(self, name: str):
        params = {
            'query': name
        }
        full_url = f"{self.url}/v1.4/movie/search"
        response = requests.get(full_url, headers=self.headers, params=params)
        # response = response.json()
        return response

#
# class ApiClass:
#     def __init__(self, url: str) -> None:
#         self.url = url or os.getenv("URL")
#
#         self.headers = {
#             "accept": "application/json",
#             "X-API-KEY": os.getenv("X_API_KEY")
#         }
#
#     def search_movies(self, name: str):
#         params = {
#             'query': name
#         }
#         full_url = f"{self.url}/v1.4/movie/search?{params}"
#         response = requests.get(full_url, headers=self.headers)
#         # resp = response.json()
#         # status_code = response[1]
#         return response