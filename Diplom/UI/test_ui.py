from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure
import pytest
from selenium import webdriver
from time import sleep


# @pytest.fixture
# def driver():
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(30)
#     browser.maximize_window()
#     yield browser
#     browser.quit()



def test_buttons_free(driver):
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
    sleep(2)
    # нажать на кнопку смотреть бесплатно CSS_SELECTOR data-test-id="SubscriptionPurchaseButton"
    button_free = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test-id="SubscriptionPurchaseButton"]'))
    )
    button_free.click()
    sleep(2)
    # нажать на кнопку узнать больше CSS_SELECTOR class="ya_5197c563 ya_7e5621e5 AuthPromo-link"
    btn_know_more = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="ya_5197c563 ya_7e5621e5 AuthPromo-link"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", btn_know_more)
    btn_know_more.click()
    sleep(2)

def test_get_trailer_to_buy(driver):
    driver.get('https://www.kinopoisk.ru/')
    wait = WebDriverWait(driver, 10)
    try:
        # Ищем кнопку капчи по CSS‑селектору
        captcha_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".CheckboxCaptcha-Button"))
        )
        captcha_button.click()
    except:
        pass

    # выбрать кнопку магазин слева href="https://hd.kinopoisk.ru/buy"
    shop_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="https://hd.kinopoisk.ru/buy"]'))
    )
    shop_btn.click()
    sleep(2)
    # нажать на фильм <a class="RouterLink_root__Buwo6 FilmPromoBlock_link__gHBOZ" # class="RouterLink_root__Buwo6 styles_button__42Cz2"
    press_film = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="RouterLink_root__Buwo6 FilmPromoBlock_link__gHBOZ"]'))
    )
    press_film.click()
    sleep(5)
    # выбрать кнопку трейлер name="Trailer"
    choose_trailer = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="Trailer"]'))
    )
    choose_trailer.click()
    sleep(2)

def test_get_top_soap(driver):
    driver.get('https://www.kinopoisk.ru/')
    wait = WebDriverWait(driver, 10)
    try:
        # Ищем кнопку капчи по CSS‑селектору
        captcha_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".CheckboxCaptcha-Button"))
        )
        captcha_button.click()
    except:
        pass

    # выбрать кнопку сериал слева (//span[@class='styles_title__Jmj_H'])[5]
    soap_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='styles_title__Jmj_H'])[5]"))
    )
    soap_btn.click()
    sleep(2)
    # нажать на 250 лучших сериалов(//span[contains(text(),'250 лучших сериалов')])[1]
    best_soap = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'250 лучших сериалов')])[1]"))
    )
    best_soap.click()
    sleep(5)
    # выбрать кнопку online (//span[contains(text(),'Онлайн')])[1]
    # проверка, что список содержит 190 сериалов
    choose_online = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Онлайн')])[1]"))
    )
    choose_online.click()
    sleep(2)


def test_correct_data(driver):

    driver.get('https://www.kinopoisk.ru/')
    sleep(5)
