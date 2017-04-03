import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def is_element_present(driver, how, what):
    try:
        driver.find_element(by=how, value=what)
    except NoSuchElementException as e:
        return False
    return True

def test_login(driver):
    driver.get("http://hrm.seleniumminutes.com/")
    username=driver.find_element_by_css_selector("#txtUsername")
    username.clear()
    username.send_keys("Admin")
    password=driver.find_element_by_css_selector("#txtPassword")
    password.clear()
    password.send_keys("Password")
    login=driver.find_element_by_css_selector("#btnLogin")
    login.click()
    assert is_element_present(driver, By.CSS_SELECTOR, "#welcome")







