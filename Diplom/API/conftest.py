from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import allure
import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Api import ApiClass
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def api():
    url = os.getenv("URL")
    return ApiClass(url)


