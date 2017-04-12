import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def testCart(driver):
    driver.get("http://localhost/litecart/en/")
    wait = WebDriverWait(driver, 5)

    n = 1
    #add products to the cart
    while int(driver.find_element_by_css_selector(".quantity").text) < 3:
        driver.find_element_by_css_selector("[id='box-most-popular'] [class='image-wrapper']").click()
        driver.find_element_by_css_selector(".quantity [type='submit']").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='cart']/a[2]/span[.= '%d']" % n)))
        n += 1
        driver.back()

    #go inside cart
    driver.find_element_by_css_selector("#cart .quantity").click()

    #delete all products from cart
    while len(driver.find_elements_by_css_selector("td.item")) > 1:
        el = driver.find_element_by_css_selector((".shortcuts li:last-child"))
        driver.find_element_by_css_selector('[name="remove_cart_item"]').click()
        wait.until(EC.staleness_of(el))






