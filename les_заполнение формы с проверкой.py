from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)
from faker import Faker

url = 'https://suninjuly.github.io/registration1.html'

driver.get(url)

#Locators
first_name = '[placeholder="Input your first name"]'
last_name = '[placeholder="Input your last name"]'
email = '[placeholder="Input your email"]'
phone = '[placeholder="Input your phone:"]'
address = '[placeholder="Input your address:"]'

wait = WebDriverWait(driver, 10)

def input_text(locator, value):
    getter = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
    getter.send_keys(value)

fake = Faker()
input_text(first_name, fake.word())
input_text(last_name, fake.word())
input_text(email, fake.word())

# Отправляем заполненную форму
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn'))).click()

# Проверка регистрации по фразе
text_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1')))
text = text_element.text
assert text == 'Congratulations! You have successfully registered!', 'Регистрация прошла неуспешно'
print('Регистрация прошла успешно')