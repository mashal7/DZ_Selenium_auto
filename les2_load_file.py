from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from faker import Faker

options = webdriver.ChromeOptions()
#options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
with webdriver.Chrome(options=options, service=service) as driver:

    url = 'http://suninjuly.github.io/file_input.html'

    driver.get(url)

    #Locators
    first_name = '//input[@name="firstname"]'
    last_name = '//input[@name="lastname"]'
    email = '//input[@name="email"]'

    wait = WebDriverWait(driver, 10)

    # Функция для получения getters
    def input_text(locator, value):
        getter = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        getter.send_keys(value)

    # Заполняем поля (обязательные)
    fake = Faker()
    input_text(first_name, fake.word())
    input_text(last_name, fake.word())
    input_text(email, fake.word())

    # Загрузка файла
    button_path = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="file"]')))
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    button_path.send_keys(file_path)
    # Отправляем заполненную форму
    driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
    time.sleep(5)

    # Проверка регистрации по фразе
    # text_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1')))
    # text = text_element.text
    # assert text == 'Congratulations! You have successfully registered!', 'Регистрация прошла неуспешно'
    # print('Регистрация прошла успешно')