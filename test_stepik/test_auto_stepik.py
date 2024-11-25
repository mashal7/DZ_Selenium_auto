import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
import math

args = ['https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1']


@pytest.mark.parametrize('url', args)
def test(driver, url):

    email = input('mail: ')
    password = input('password: ')
    driver.get(url)
    #driver.set_page_load_timeout(5)

    #Locators
    input_button = '//a[@class="ember-view navbar__auth navbar__auth_login st-link st-link_style_button"]'
    email_field = '//input[@name="login"]'
    password_field = '//input[@name="password"]'


    wait = WebDriverWait(driver, 10)

    def input_text(locator, value):
        getter = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        getter.send_keys(value)


    # Нажимаем кнопку войти
    wait.until(EC.visibility_of_element_located((By.XPATH, input_button))).click()

    # Авторизация
    input_text(email_field, email)
    input_text(password_field, password)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.sign-form__btn.button_with-loader '))).click()

    # ввод ответа
    answer = math.log(int(time.time()))
    print(answer)
    time.sleep(5)
    input_text('//textarea[@class="ember-text-area ember-view textarea string-quiz__textarea"]', answer)
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))).click()

    # Проверка ответа
    text_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))
    text = text_element.text
    assert text == 'Correct!', 'Текст не совпадает. Ответ неверный'
    print('Текст совпадает. Ответ верный')




