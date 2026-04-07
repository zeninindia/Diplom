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

    # assert что при нажатии на кнопку онлайн кинотеатр открывается страница с url = https://hd.kinopoisk.ru/
    # assert что на странице есть сообщение "30 дней бесплатно"
    # assert что на кнопке написано "Попробовать бесплатно"
    )
    online_cinema_btn.click()
    sleep(2)
    # нажать на кнопку смотреть бесплатно CSS_SELECTOR data-test-id="SubscriptionPurchaseButton"
    button_free = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test-id="SubscriptionPurchaseButton"]'))
    )
    button_free.click()
    sleep(2)

    # assert  что нажатие на кнопку "попробовать бесплатно" переходит на сайт вот с таким url = https://passport.yandex.ru/pwl-yandex/auth/add?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fhd.kinopoisk.ru%252F%26uuid%3D6163884d-4f5f-4936-8bea-a7e21a45aa0a&cause=auth&process_uuid=50f01302-002b-4f21-94b2-2491bd976d9b
    # assert что есть сообщение на странице "Яндекс ID — ключ для всех сервисов"

    # нажать на кнопку узнать больше CSS_SELECTOR class="ya_5197c563 ya_7e5621e5 AuthPromo-link"
    btn_know_more = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="ya_5197c563 ya_7e5621e5 AuthPromo-link"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", btn_know_more)
    btn_know_more.click()
    # assert что нажатие на кнопку "узнать больше" открывается страница с url = https://yandex.ru/id/about
    # assert что на странице есть плашка, кнопка "в приложении - удобнее"

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

    # assert что есть кнопка на которой написано "Смотреть кино бесплатно"
    # assert что на странице фильма на постере написано
    #    описание "class="ContentOverview_description__CXd5E" c текстом....
    # assert
    # assert

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

    # assert
    # assert
    # assert
    # assert
    # assert



def test_correct_data(driver):

    driver.get('https://www.kinopoisk.ru/')
    sleep(5)

