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

def test_sort(driver):
    driver.get("http://360rideshop.com/man-burton.html")
    list = driver.find_elements_by_css_selector("[itemprop='headline']")
    el = [e.text for e in list]
    assert all('Burton' in x for x in el)







