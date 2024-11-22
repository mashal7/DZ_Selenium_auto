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

    url = 'http://suninjuly.github.io/execute_script.html'
    driver.get(url)

    # Locators
    x_locator = '//span[@id="input_value"]'

    wait = WebDriverWait(driver, 10)


    # Функция для счета
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    # Функция для получения getters
    def getter(locator):
        return wait.until(EC.visibility_of_element_located((By.XPATH, locator)))


    # получение x и ввод значения
    value = calc(int(getter(x_locator).text))
    getter('//input[@id="answer"]').send_keys(value)


    # Checkbox, radiobutton
    checkbox = getter('//input[@id="robotCheckbox"]').click()

    # Прокрутка из-за футера
    button = getter('//input[@id="robotsRule"]')
    #driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Отправляем заполненную форму
    getter('//button[@class="btn btn-primary"]').click()
    time.sleep(5)