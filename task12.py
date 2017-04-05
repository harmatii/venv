import pytest
from selenium import webdriver
import os.path
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

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

def testAddNew(driver):
    driver.get("http://localhost/litecart/admin")
    username = driver.find_element_by_name("username").send_keys("admin")
    password = driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//span[.='Catalog']").click()
    driver.find_element_by_xpath("//td[@id='content'] //a[2]").click()
    driver.find_element_by_css_selector("tr label [value='1']").click()
    driver.find_element_by_css_selector("[name='name[en]']").send_keys("New Test Duck")
    driver.find_element_by_css_selector("[name='code']").send_keys("12345")
    driver.find_element_by_css_selector("[data-name='Rubber Ducks']").click()
    driver.find_element_by_css_selector("[data-name='Subcategory']").click()
    driver.find_element_by_css_selector("td [value= '1-3']").click()
    quantity = driver.find_element_by_css_selector("[name='quantity']")
    quantity.clear()
    quantity.send_keys("1")
    driver.find_element_by_css_selector("[name='new_images[]']")\
        .send_keys(os.path.abspath("testimg.png"))
    driver.find_element_by_css_selector("[name='date_valid_from']").send_keys("04032017")
    driver.find_element_by_css_selector("[name='date_valid_to']").send_keys("04032019")
    driver.find_element_by_css_selector("[name='save']").click()

    driver.find_element_by_xpath("//a[.= 'New Test Duck']").click()
    driver.find_element_by_xpath("//a[.= 'Information']").click()
    driver.find_element_by_xpath("//option[.= 'ACME Corp.']").click()
    driver.find_element_by_css_selector("[name='keywords']").send_keys("testduck")
    driver.find_element_by_css_selector("[name='short_description[en]']").send_keys("testduck")
    driver.find_element_by_css_selector(".trumbowyg-editor").send_keys("testduck")
    driver.find_element_by_css_selector("[name='head_title[en]']").send_keys("testduck")
    driver.find_element_by_css_selector("[name='meta_description[en]']").send_keys("testduck")
    driver.find_element_by_css_selector("[name='save']").click()

    driver.find_element_by_xpath("//a[.= 'New Test Duck']").click()
    driver.find_element_by_xpath("//a[.= 'Prices']").click()
    purchase_price = driver.find_element_by_css_selector("[name='purchase_price']")
    purchase_price.clear()
    purchase_price.send_keys("7.00")
    driver.find_element_by_css_selector("[value='USD']").click()
    pricesUSD = driver.find_element_by_css_selector("[name='prices[USD]']")
    pricesUSD.clear()
    pricesUSD.send_keys("7.00")
    pricesEUR = driver.find_element_by_css_selector("[name='prices[EUR]']")
    pricesEUR.clear()
    pricesEUR.send_keys("6.00")
    driver.find_element_by_css_selector("[name='save']").click()
    assert is_element_present(driver, By.XPATH, "//a[.= 'New Test Duck']")
