import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import math
from selenium.webdriver.common.alert import Alert

options = webdriver.ChromeOptions()
#options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
with webdriver.Chrome(options=options, service=service) as driver:

    url = 'http://suninjuly.github.io/explicit_wait2.html'
    driver.get(url)

    # Locators
    x_locator = '//span[@id="input_value"]'

    wait = WebDriverWait(driver, 15)


    # Функция для счета
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    # Функция для получения getters
    def getter(locator):
        return wait.until(EC.visibility_of_element_located((By.XPATH, locator)))


    # дождаться цены 100$
    price = driver.find_element(By.XPATH, '//h5[@id="price"]')
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//h5[@id="price"]'), '$100'))
    getter('//button[@id="book" and @class="btn btn-primary"]').click()

    # получение x и ввод значения
    value = calc(int(getter(x_locator).text))
    getter('//input[@id="answer"]').send_keys(value)

    # Отправляем заполненную форму
    getter('//button[@id="solve" and @class="btn btn-primary"]').click()
    time.sleep(5)