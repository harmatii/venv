import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def testCountries(driver):
    driver.get("http://localhost/litecart/admin")
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("admin")
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("admin")
    driver.find_element_by_name("login").click()

    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    elements = driver.find_elements_by_css_selector("td:nth-child(5)")
    names = [e.text for e in elements]
    assert names == sorted(names)

    driver.find_element_by_link_text("Canada").click()
    elements = driver.find_elements_by_css_selector("td:nth-child(3)")
    del elements[0]
    del elements[13]
    names = [e.text for e in elements]
    assert names == sorted(names)
    driver.back()

    driver.find_element_by_link_text("United States").click()
    elements = driver.find_elements_by_css_selector("td:nth-child(3)")
    del elements[0]
    del elements[65]
    names = [e.text for e in elements]
    assert names == sorted(names)