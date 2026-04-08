from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import allure
import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    browser.maximize_window()
    yield browser
    browser.quit()

