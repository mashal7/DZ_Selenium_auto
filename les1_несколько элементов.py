from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import math

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)
from faker import Faker

url = 'http://suninjuly.github.io/huge_form.html'

driver.get(url)

#Locators
first_name = '[name="first_name"]'
last_name = '[name="last_name"]'
city = '.form-control.city'
country = '#country.form-control'
link = str(math.ceil(math.pow(math.pi, math.e)*10000))

wait = WebDriverWait(driver, 10)

getters = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
fake = Faker()

for getter in getters:
    getter.send_keys(fake.word())

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-default'))).click()