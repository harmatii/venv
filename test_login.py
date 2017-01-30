import pytest
from selenium import webdriver



@pytest.fixture
def wd(request):
    driver = webdriver.Firefox()
    request.addfinalizer(driver.quit)
    return driver


def test_login(wd):
    wd.get("http://localhost/litecart/admin/login.php")
    username = wd.find_element_by_name("username")
    username.clear()
    username.send_keys("admin")
    password = wd.find_element_by_name("password")
    password.clear()
    password.send_keys("password")
    login = wd.find_element_by_name("login")
    login.click()

