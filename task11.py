import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.color import Color


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def testnewUser(driver):
    driver.get("http://localhost/litecart/en/")
    driver.find_element_by_link_text("New customers click here").click()
    firstname = driver.find_element_by_css_selector("[name=firstname]").send_keys("Ihor")
    lastname = driver.find_element_by_css_selector("[name=lastname]").send_keys("Harmatii")
    address = driver.find_element_by_css_selector("[name=address1]").send_keys("11 Warring Dr")
    postcode = driver.find_element_by_css_selector("[name=postcode]").send_keys("10509")
    city = driver.find_element_by_css_selector("[name=city]").send_keys("Carmel")
    country = driver.find_element_by_css_selector(".select2-selection__arrow").click()
    countryselect = driver.find_element_by_xpath("//li[.='United States']").click()
    email = driver.find_element_by_css_selector("[name=email]").send_keys("igorko112@gmail.com")
    phone = driver.find_element_by_css_selector("[name=phone]").send_keys("+79854763245")
    pass1 = driver.find_element_by_css_selector("[name=password]").send_keys("12345678")
    pass2 = driver.find_element_by_css_selector("[name=confirmed_password]").send_keys("12345678")
    create = driver.find_element_by_css_selector("[name=create_account]").click()
    logout = driver.find_element_by_xpath("//a[.='Logout']").click()
    logn = driver.find_element_by_css_selector("[name=email]").send_keys("igorko112@gmail.com")
    passin = driver.find_element_by_css_selector("[name=password]").send_keys("12345678")
    driver.find_element_by_xpath("//button[.='Login']").click()
    logut = driver.find_element_by_xpath("//a[.='Logout']").click()