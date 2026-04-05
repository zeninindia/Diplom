from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
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
# class="CheckboxCaptcha-Button"


def test_ui_1(driver):
    driver.get('https://www.kinopoisk.ru/?utm_referrer=organic.kinopoisk.ru')
    wait = WebDriverWait(driver, 5)
    try:
        # Ищем кнопку капчи по CSS‑селектору
        captcha_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".CheckboxCaptcha-Button"))
        )
        captcha_button.click()
    except:
        pass

    # нажать на кнопку 'Онлайн-кинотеатр' XPATH (//a[contains(text(),'Онлайн-кинотеатр')])[1]
    online_cinema_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Онлайн-кинотеатр')]"))
    )
    online_cinema_btn.click()
    # нажать на кнопку смотреть бесплатно CSS_SELECTOR data-test-id="SubscriptionPurchaseButton"
    button_free = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test-id="SubscriptionPurchaseButton"]'))
    )
    button_free.click()
    # нажать на кнопку узнать больше CSS_SELECTOR class="ya_5197c563 ya_7e5621e5 AuthPromo-link"
    btn_know_more = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="ya_5197c563 ya_7e5621e5 AuthPromo-link"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", btn_know_more)
    btn_know_more.click()
