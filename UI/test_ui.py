from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
import allure
import selenium
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    browser.maximize_window()
    yield browser
    browser.quit()
# class="CheckboxCaptcha-Button"


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
# https://www.kinopoisk.ru/showcaptcha?cc=1&form-fb-hint=8.20&mt=B89CD5602DED40E185F917127623580E40F99992398A9385EE2C097D4C2AAD78512C6003874066EB948DEC8829F3BA67F3EB9D7BC4DBA7B1211EDDAB5BC868B572B013F76DF7609F442419178FA9CE16CE83E88F72925A9931175DB85965F93DDB76AD0B5D63D15954D23A9531E884ABAC581B271D3B721893074F0A125340F149A164E3E0B88B3371F9B761277834017D757C2B3DEA968622A5246BDB077DDD93F326E9C3BD6C2B685A161C2C1415CC6A1347569774F4CFD6B104677B74ED2AFA4876270607D5D13A040070BCC7126F5FD376A561A5F2912096CC51&retpath=aHR0cHM6Ly93d3cua2lub3BvaXNrLnJ1Lz91dG1fcmVmZXJyZXI9b3JnYW5pYy5raW5vcG9pc2sucnU%2C_5f4b30506f7a45e6ef5cbdecba6c7e55&t=2%252F1775349591%252Fee2101bc8f4eefd7596ef981b504a030&u=8461229818189377225&s=76d5838386b69e2a28fb32e879c995af