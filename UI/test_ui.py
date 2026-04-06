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
    # проверка, что список содержит список сериалов(что количество совпадает с цифрой)
    choose_online = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Онлайн')])[1]"))
    )
    choose_online.click()
    sleep(5)


def test_correct_data(driver):

    driver.get('https://www.kinopoisk.ru/')
    sleep(5)
# заходим на страничку выбора пользователя url = https://passport.yandex.ru/pwl-yandex/auth/list?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fwww.kinopoisk.ru%252F%253Futm_referrer%253Dorganic.kinopoisk.ru%26uuid%3D06c4a670-1396-4ef2-a514-37111d6db487&cause=auth&process_uuid=9ce397b1-05a8-4a9c-911e-1e124f28ac43
# и проверяем, что в табличке указан email & login name

# kp_cookie = yuidss=9780504781707849214; gdpr=0; _ym_uid=1707856549319105610; yandexuid=9780504781707849214; adrdel=1743529368661; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1743615768676%2C%22sl%22%3A%7B%22224%22%3A1743529368676%2C%221228%22%3A1743529368676%7D%7D; is_gdpr=0; is_gdpr_b=CJzWUhDYywIoAg==; my=YycCAAEA; _ym_d=1763284145; yashr=2870412211771455629; ymex=2086815631.yrts.1771455631; amcuid=9559710491771713860; yandex_login=zeninindia2; alice_uuid=D3C773E1-D4F7-46A2-A658-7B5515285E1C; i=zyW8ZuJVSyLr7rOm33vKP/0z4FsuHuOrK9NQOdsricBObcnMF9ZJ1Sbf0fUjpA7A32F84ja/Jr2Y5a/77/j8fEa7GPU=; isa=Y3zs3PFtc0vSARB6+Qb/PzMj7vfdLs9SlAfTIiXMqjlxJ6voiXv5416Rbu5lLTQeP9MfAiuCxMH2OUiTXOHvC4eONcA=; sae=0:D3C773E1-D4F7-46A2-A658-7B5515285E1C:p:26.3.2.773:w:d:RU:20230103; pi=hTzF3fttwM7a5NEU2afzxHLhviWnDL0ZhobHwOUe1iJyDTyFNq69ilSSigiTvrJ+AhkyyMIwQGId4uHRt6XGW0DG+M0=; Session_id=3:1775387461.5.0.1773290006494:3InyXg:3c83.1.2:1|1187574294.-1.2.3:1773290006|3:11820438.353848.-FU16hYkGP2KiNpBzk2NKAChBjg; sessar=1.1719225.CiCxGltBzEyx53cWGzh0XnJOAJR0NXH_gBFQumu77S_ZuQ.1Wid5JQ5gQuaOp7X6uhhpTkaZf1SRgNoCA5TuX3IINE; sessionid2=3:1775387461.5.0.1773290006494:3InyXg:3c83.1.2:1|1187574294.-1.2.3:1773290006|3:11820438.353848.fakesign0000000000000000000; _ym_isad=2; ys=udn.cDp6ZW5pbmluZGlhMg%3D%3D#c_chck.1019518506; yp=1789405512.brd.6102004825#1782245161.cld.2270452#1782945363.dafs.12-3_25-3#1794820145.dc_neuro.9#1776001332.dlp.3#1775419201.duc.ru#1775421542.gpauto.59_939179:30_267092:96:0:1775414342#1777815733.hdrc.1#2048863560.hks.0#2040120979.multib.1#2090706910.pcs.0#1803028492.swntab.0#1779052144.sz.1280x720x1_5#1788262228.szm.1_5:1280x720:0x0:0#1775419201.uc.ru#2088650006.udn.cDp6ZW5pbmluZGlhMg%3D%3D; gpauto=59_939179:30_267092:96:0:1775414342; alice_reqids=1775414607740842-7901752793381212103-yirgezdynobb46j4-BAL.1775414607~1775354455505581-1944495442627282382-jcmpmmh7qrx2tejf-BAL.1775354455; bh=Ek8iTm90KEE6QnJhbmQiO3Y9IjgiLCAiQ2hyb21pdW0iO3Y9IjE0NCIsICJZYUJyb3dzZXIiO3Y9IjI2LjMiLCAiWW93c2VyIjt2PSIyLjUiGgUieDg2IiIKMjYuMy4yLjc3MyoCPzAyAiIiOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUmYiTm90KEE6QnJhbmQiO3Y9IjguMC4wLjAiLCAiQ2hyb21pdW0iO3Y9IjE0NC4wLjc1NTkuNzczIiwgIllhQnJvd3NlciI7dj0iMjYuMy4yLjc3MyIsICJZb3dzZXIiO3Y9IjIuNSJaAj8wYNLays4GaiHcyuH/CJLYobEDn8/h6gP7+vDnDev//fYPnvfNlAfzgQI=
# kp_cookie = yuidss=9780504781707849214; gdpr=0; _ym_uid=1707856549319105610; yandexuid=9780504781707849214; adrdel=1743529368661; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1743615768676%2C%22sl%22%3A%7B%22224%22%3A1743529368676%2C%221228%22%3A1743529368676%7D%7D; is_gdpr=0; is_gdpr_b=CJzWUhDYywIoAg==; my=YycCAAEA; _ym_d=1763284145; yashr=2870412211771455629; ymex=2086815631.yrts.1771455631; amcuid=9559710491771713860; yandex_login=zeninindia2; alice_uuid=D3C773E1-D4F7-46A2-A658-7B5515285E1C; i=zyW8ZuJVSyLr7rOm33vKP/0z4FsuHuOrK9NQOdsricBObcnMF9ZJ1Sbf0fUjpA7A32F84ja/Jr2Y5a/77/j8fEa7GPU=; isa=Y3zs3PFtc0vSARB6+Qb/PzMj7vfdLs9SlAfTIiXMqjlxJ6voiXv5416Rbu5lLTQeP9MfAiuCxMH2OUiTXOHvC4eONcA=; sae=0:D3C773E1-D4F7-46A2-A658-7B5515285E1C:p:26.3.2.773:w:d:RU:20230103; pi=hTzF3fttwM7a5NEU2afzxHLhviWnDL0ZhobHwOUe1iJyDTyFNq69ilSSigiTvrJ+AhkyyMIwQGId4uHRt6XGW0DG+M0=; Session_id=3:1775387461.5.0.1773290006494:3InyXg:3c83.1.2:1|1187574294.-1.2.3:1773290006|3:11820438.353848.-FU16hYkGP2KiNpBzk2NKAChBjg; sessar=1.1719225.CiCxGltBzEyx53cWGzh0XnJOAJR0NXH_gBFQumu77S_ZuQ.1Wid5JQ5gQuaOp7X6uhhpTkaZf1SRgNoCA5TuX3IINE; sessionid2=3:1775387461.5.0.1773290006494:3InyXg:3c83.1.2:1|1187574294.-1.2.3:1773290006|3:11820438.353848.fakesign0000000000000000000; _ym_isad=2; alice_reqids=1775414607740842-7901752793381212103-yirgezdynobb46j4-BAL.1775414607~1775354455505581-1944495442627282382-jcmpmmh7qrx2tejf-BAL.1775354455; yp=1789405512.brd.6102004825#1782245161.cld.2270452#1782945363.dafs.12-3_25-3#1794820145.dc_neuro.9#1776001332.dlp.3#1775419201.duc.ru#1775422142.gpauto.59_939179:30_267092:96:0:1775414942#1777815733.hdrc.1#2048863560.hks.0#2040120979.multib.1#2090706910.pcs.0#1803028492.swntab.0#1779052144.sz.1280x720x1_5#1788262228.szm.1_5:1280x720:0x0:0#1775419201.uc.ru#2088650006.udn.cDp6ZW5pbmluZGlhMg%3D%3D; gpauto=59_939179:30_267092:96:0:1775414942; ys=udn.cDp6ZW5pbmluZGlhMg%3D%3D#c_chck.2380673188; bh=Ek8iTm90KEE6QnJhbmQiO3Y9IjgiLCAiQ2hyb21pdW0iO3Y9IjE0NCIsICJZYUJyb3dzZXIiO3Y9IjI2LjMiLCAiWW93c2VyIjt2PSIyLjUiGgUieDg2IiIKMjYuMy4yLjc3MyoCPzAyAiIiOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUmYiTm90KEE6QnJhbmQiO3Y9IjguMC4wLjAiLCAiQ2hyb21pdW0iO3Y9IjE0NC4wLjc1NTkuNzczIiwgIllhQnJvd3NlciI7dj0iMjYuMy4yLjc3MyIsICJZb3dzZXIiO3Y9IjIuNSJaAj8wYNjhys4GaiHcyuH/CJLYobEDn8/h6gP7+vDnDev//fYPnvfNlAfzgQI=
# y_cookie = yuidss=9780504781707849214; gdpr=0; _ym_uid=1707856549319105610; yandexuid=9780504781707849214; adrdel=1743529368661; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1743615768676%2C%22sl%22%3A%7B%22224%22%3A1743529368676%2C%221228%22%3A1743529368676%7D%7D; is_gdpr=0; is_gdpr_b=CJzWUhDYywIoAg==; my=YycCAAEA; _ym_d=1763284145; yashr=2870412211771455629; ymex=2086815631.yrts.1771455631; amcuid=9559710491771713860; yandex_login=zeninindia2; alice_uuid=D3C773E1-D4F7-46A2-A658-7B5515285E1C; i=zyW8ZuJVSyLr7rOm33vKP/0z4FsuHuOrK9NQOdsricBObcnMF9ZJ1Sbf0fUjpA7A32F84ja/Jr2Y5a/77/j8fEa7GPU=; isa=Y3zs3PFtc0vSARB6+Qb/PzMj7vfdLs9SlAfTIiXMqjlxJ6voiXv5416Rbu5lLTQeP9MfAiuCxMH2OUiTXOHvC4eONcA=; sae=0:D3C773E1-D4F7-46A2-A658-7B5515285E1C:p:26.3.2.773:w:d:RU:20230103; Session_id=3:1775387461.5.0.1773290006494:3InyXg:3c83.1.2:1|1187574294.-1.2.3:1773290006|3:11820438.353848.-FU16hYkGP2KiNpBzk2NKAChBjg; sessar=1.1719225.CiCxGltBzEyx53cWGzh0XnJOAJR0NXH_gBFQumu77S_ZuQ.1Wid5JQ5gQuaOp7X6uhhpTkaZf1SRgNoCA5TuX3IINE; sessionid2=3:1775387461.5.0.1773290006494:3InyXg:3c83.1.2:1|1187574294.-1.2.3:1773290006|3:11820438.353848.fakesign0000000000000000000; _ym_isad=2; alice_reqids=1775414607740842-7901752793381212103-yirgezdynobb46j4-BAL.1775414607~1775354455505581-1944495442627282382-jcmpmmh7qrx2tejf-BAL.1775354455; yp=1789405512.brd.6102004825#1782245161.cld.2270452#1782945363.dafs.12-3_25-3#1794820145.dc_neuro.9#1776001332.dlp.3#1775419201.duc.ru#1775422142.gpauto.59_939179:30_267092:96:0:1775414942#1777815733.hdrc.1#2048863560.hks.0#2040120979.multib.1#2090706910.pcs.0#1803028492.swntab.0#1779052144.sz.1280x720x1_5#1788262228.szm.1_5:1280x720:0x0:0#1775419201.uc.ru#2088650006.udn.cDp6ZW5pbmluZGlhMg%3D%3D; gpauto=59_939179:30_267092:96:0:1775414942; ys=udn.cDp6ZW5pbmluZGlhMg%3D%3D#c_chck.2380673188; pi=i3vSM5p2zSN4pysZMvGBAff9poiCHp8xqlMULV6PhQqjsL4oGUCAAcqfamhgaU8wk9wffkLK8ULD4nYcJVe0ZtV0XJk=; bh=Ek8iTm90KEE6QnJhbmQiO3Y9IjgiLCAiQ2hyb21pdW0iO3Y9IjE0NCIsICJZYUJyb3dzZXIiO3Y9IjI2LjMiLCAiWW93c2VyIjt2PSIyLjUiGgUieDg2IiIKMjYuMy4yLjc3MyoCPzAyAiIiOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUmYiTm90KEE6QnJhbmQiO3Y9IjguMC4wLjAiLCAiQ2hyb21pdW0iO3Y9IjE0NC4wLjc1NTkuNzczIiwgIllhQnJvd3NlciI7dj0iMjYuMy4yLjc3MyIsICJZb3dzZXIiO3Y9IjIuNSJaAj8wYJzgys4GaiHcyuH/CJLYobEDn8/h6gP7+vDnDev//fYPnvfNlAfzgQI=
# https://www.kinopoisk.ru/showcaptcha?cc=1&form-fb-hint=8.20&mt=B89CD5602DED40E185F917127623580E40F99992398A9385EE2C097D4C2AAD78512C6003874066EB948DEC8829F3BA67F3EB9D7BC4DBA7B1211EDDAB5BC868B572B013F76DF7609F442419178FA9CE16CE83E88F72925A9931175DB85965F93DDB76AD0B5D63D15954D23A9531E884ABAC581B271D3B721893074F0A125340F149A164E3E0B88B3371F9B761277834017D757C2B3DEA968622A5246BDB077DDD93F326E9C3BD6C2B685A161C2C1415CC6A1347569774F4CFD6B104677B74ED2AFA4876270607D5D13A040070BCC7126F5FD376A561A5F2912096CC51&retpath=aHR0cHM6Ly93d3cua2lub3BvaXNrLnJ1Lz91dG1fcmVmZXJyZXI9b3JnYW5pYy5raW5vcG9pc2sucnU%2C_5f4b30506f7a45e6ef5cbdecba6c7e55&t=2%252F1775349591%252Fee2101bc8f4eefd7596ef981b504a030&u=8461229818189377225&s=76d5838386b69e2a28fb32e879c995af