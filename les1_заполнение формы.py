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

url = 'https://suninjuly.github.io/simple_form_find_task.html'

driver.get(url)

#Locators
first_name = '[name="first_name"]'
last_name = '[name="last_name"]'
city = '.form-control.city'
country = '#country.form-control'

wait = WebDriverWait(driver, 10)

def input_text(locator, value):
    getter = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
    getter.send_keys(value)

input_text(first_name, 'Maria')
input_text(last_name, 'Petrova')
input_text(city, 'Moscow')
input_text(country, 'Russia')

# Отправляем заполненную форму
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#submit_button'))).click()

