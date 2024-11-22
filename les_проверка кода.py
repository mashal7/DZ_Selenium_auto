from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
from faker import Faker

options = webdriver.ChromeOptions()
#options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
with webdriver.Chrome(options=options, service=service) as driver:

    #url = 'http://suninjuly.github.io/registration1.html'

    # с ошибкой
    #url = 'http://suninjuly.github.io/registration2.html'

    driver.get(url)

    #Locators
    first_name = '.first_block .first_class [type="text"]'
    last_name = '.first_block .second_class [type="text"]'
    email = '.first_block .third_class [type="text"]'
    phone = '.second_block .first_class [type="text"]'
    address = '.second_block .second_class [type="text"]'

    wait = WebDriverWait(driver, 10)

    # Функция для получения getters
    def input_text(locator, value):
        #getter = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        getter = driver.find_element(By.CSS_SELECTOR, locator)
        getter.send_keys(value)

    # Заполняем поля (обязательные)
    fake = Faker()
    input_text(first_name, fake.word())
    input_text(last_name, fake.word())
    input_text(email, fake.word())

    # необязательные
    # input_text(phone, fake.word())
    # input_text(address, fake.word())


    # Отправляем заполненную форму
    driver.find_element(By.CSS_SELECTOR, 'button.btn').click()

    # Проверка регистрации по фразе
    text_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1')))
    text = text_element.text
    assert text == 'Congratulations! You have successfully registered!', 'Регистрация прошла неуспешно'
    print('Регистрация прошла успешно')