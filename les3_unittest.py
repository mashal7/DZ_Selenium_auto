from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
from faker import Faker
import unittest


class TestAbs(unittest.TestCase):

    # Locators
    first_name = '.first_block .first_class [type="text"]'
    last_name = '.first_block .second_class [type="text"]'
    email = '.first_block .third_class [type="text"]'
    phone = '.second_block .first_class [type="text"]'
    address = '.second_block .second_class [type="text"]'

    def setUp(self):
        """Настройка перед каждым тестом"""
        options = webdriver.ChromeOptions()
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(options=options, service=self.service)
        self.fake = Faker()
        self.wait = WebDriverWait(self.driver, 10)

    def input_text(self, locator, value):
        # getter = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        getter = self.driver.find_element(By.CSS_SELECTOR, locator)
        getter.send_keys(value)

    def quit_browser(self):
        self.driver.quit()

    def test_registration_correct(self):
        url = 'http://suninjuly.github.io/registration1.html'

        # с ошибкой
        #url = 'http://suninjuly.github.io/registration2.html'
        self.driver.get(url)

        # Заполняем поля (обязательные)
        fake = Faker()
        self.input_text(self.first_name, fake.word())
        self.input_text(self.last_name, fake.word())
        self.input_text(self.email, fake.word())
        # необязательные
        # input_text(phone, fake.word())
        # input_text(address, fake.word())

        # Отправляем заполненную форму
        self.driver.find_element(By.CSS_SELECTOR, 'button.btn').click()

        # Проверка регистрации по фразе
        text_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1')))
        text = text_element.text
        self.assertEqual(
            text_element.text,'Congratulations! You have successfully registered!',
            'Регистрация прошла неуспешно')
        print('Регистрация прошла успешно')

    def test_registration_wrong(self):

        url = 'http://suninjuly.github.io/registration2.html'
        self.driver.get(url)

        # Заполняем поля (обязательные)
        fake = Faker()
        self.input_text(self.first_name, fake.word())
        self.input_text(self.last_name, fake.word())
        self.input_text(self.email, fake.word())
        # необязательные
        # input_text(phone, fake.word())
        # input_text(address, fake.word())

        # Отправляем заполненную форму
        self.driver.find_element(By.CSS_SELECTOR, 'button.btn').click()

        # Проверка регистрации по фразе
        text_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1')))
        text = text_element.text
        self.assertEqual(
            text_element.text, 'Congratulations! You have successfully registered!',
            'Регистрация прошла неуспешно')
        print('Регистрация прошла успешно')

if __name__ == "__main__":
    unittest.main()