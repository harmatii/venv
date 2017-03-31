import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def testZones(driver):
    driver.get("http://localhost/litecart/admin")
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("admin")
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("admin")
    driver.find_element_by_name("login").click()

    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.find_element_by_link_text("Canada").click()
    el = driver.find_elements_by_css_selector("td:nth-child(3)")
    del el[0]
    names = [e.text for e in el]
    assert names == sorted(names)
    driver.back()

    driver.find_element_by_link_text("United States of America").click()
    el = driver.find_elements_by_css_selector("td:nth-child(3)")
    del el[0]
    names = [e.text for e in el]
    assert names == sorted(names)