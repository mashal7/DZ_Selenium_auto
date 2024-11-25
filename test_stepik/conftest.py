import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture
def driver():
    print('Start test')

    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.page_load_strategy = 'eager'
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)

    yield driver
    time.sleep(6)
    driver.quit()
    print('Finish test')

# @pytest.mark.parametrize('set_up', args, indirect=True)
# def test_with_url(set_up):
#     driver.get(url)