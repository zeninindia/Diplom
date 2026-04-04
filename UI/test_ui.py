from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure
import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def browser():
    driver = selenium.webdriver.Chrome()
    driver.maximize_window()
    return driver

def test_ui_1(browser):
    browser = selenium.webdriver.Chrome()
