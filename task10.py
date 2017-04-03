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


def testProduct(driver):
    driver.get("http://localhost/litecart/en/")

    #а) на главной странице и на странице товара совпадает текст названия товара
    mainpage = driver.find_element_by_css_selector("#box-campaigns .name").text
    driver.find_element_by_css_selector("#box-campaigns .name").click()
    productpage = driver.find_element_by_css_selector("h1[class=title]").text
    assert mainpage == productpage
    driver.back()

    #б) на главной странице и на странице товара совпадают цены (обычная и акционная)
    price = driver.find_element_by_css_selector(".regular-price").text
    saleprice = driver.find_element_by_css_selector(".campaign-price").text
    driver.find_element_by_css_selector("#box-campaigns .name").click()
    pricein = driver.find_element_by_css_selector(".regular-price").text
    salepricein = driver.find_element_by_css_selector(".campaign-price").text
    assert price == pricein
    assert saleprice == salepricein
    driver.back()

    #в) обычная цена зачёркнутая и серая
    textdec = driver.find_element_by_css_selector(".regular-price").value_of_css_property("text-decoration")
    assert textdec == "line-through"
    colorprice = Color.from_string(driver.find_element_by_css_selector(".regular-price").value_of_css_property("color"))
    assert colorprice.red == colorprice.green == colorprice.blue
    driver.find_element_by_css_selector("#box-campaigns .name").click()
    textdec = driver.find_element_by_css_selector(".regular-price").value_of_css_property("text-decoration")
    assert textdec == "line-through"
    colorprice = Color.from_string(driver.find_element_by_css_selector(".regular-price").value_of_css_property("color"))
    assert colorprice.red == colorprice.green == colorprice.blue
    driver.back()

    # #г) акционная жирная и красная
    textfont = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("font-weight")
    assert textfont == "bold"
    colorsaleprice = Color.from_string(
        driver.find_element_by_css_selector(".campaign-price").value_of_css_property("color"))
    assert colorsaleprice.green == colorsaleprice.blue == 0
    driver.find_element_by_css_selector("#box-campaigns .name").click()
    textfont = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("font-weight")
    assert textfont == "bold"
    colorsaleprice = Color.from_string(
        driver.find_element_by_css_selector(".campaign-price").value_of_css_property("color"))
    assert colorsaleprice.green == colorsaleprice.blue == 0
    driver.back()

    # #г) акционная цена крупнее, чем обычная
    fontsaleprice = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size")
    fontprice = driver.find_element_by_css_selector(".regular-price").value_of_css_property("font-size")
    assert fontsaleprice > fontprice
    driver.find_element_by_css_selector("#box-campaigns .name").click()
    fontsaleprice = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size")
    fontprice = driver.find_element_by_css_selector(".regular-price").value_of_css_property("font-size")
    assert fontsaleprice > fontprice
