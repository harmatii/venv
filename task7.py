import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def testall(driver):
    driver.get("http://localhost/litecart/admin")
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("admin")
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("admin")
    driver.find_element_by_name("login").click()

    driver.find_element_by_xpath("//span[.='Appearence']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Template" in h1)
    driver.find_element_by_css_selector("#doc-template").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Template" in h1)
    driver.find_element_by_css_selector("#doc-logotype").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Logotype" in h1)
    driver.find_element_by_xpath("//span[.='Catalog']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Catalog" in h1)
    driver.find_element_by_css_selector("#doc-catalog").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Catalog" in h1)
    driver.find_element_by_css_selector("#doc-product_groups").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Product Groups" in h1)
    driver.find_element_by_css_selector("#doc-option_groups").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Option Groups" in h1)
    driver.find_element_by_css_selector("#doc-manufacturers").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Manufacturers" in h1)
    driver.find_element_by_css_selector("#doc-suppliers").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Suppliers" in h1)
    driver.find_element_by_css_selector("#doc-delivery_statuses").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Delivery Statuses" in h1)
    driver.find_element_by_css_selector("#doc-sold_out_statuses").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Sold Out Statuses" in h1)
    driver.find_element_by_css_selector("#doc-quantity_units").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Quantity Units" in h1)
    driver.find_element_by_css_selector("#doc-csv").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("CSV Import/Export" in h1)
    driver.find_element_by_xpath("//span[.='Countries']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Countries" in h1)
    driver.find_element_by_xpath("//span[.='Currencies']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Currencies" in h1)
    driver.find_element_by_xpath("//span[.='Customers']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Customers" in h1)
    driver.find_element_by_css_selector("#doc-customers").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Customers" in h1)
    driver.find_element_by_css_selector("#doc-csv").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("CSV Import/Export" in h1)
    driver.find_element_by_css_selector("#doc-newsletter").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Newsletter" in h1)
    driver.find_element_by_xpath("//span[.='Geo Zones']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Geo Zones" in h1)
    driver.find_element_by_xpath("//span[.='Languages']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Languages" in h1)
    driver.find_element_by_css_selector("#doc-languages").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Languages" in h1)
    driver.find_element_by_css_selector("#doc-storage_encoding").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Storage Encoding" in h1)
    driver.find_element_by_xpath("//span[.='Modules']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Job Modules" in h1)
    driver.find_element_by_css_selector("#doc-jobs").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Job Modules" in h1)
    driver.find_element_by_css_selector("#doc-customer").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Customer Modules" in h1)
    driver.find_element_by_css_selector("#doc-shipping").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Shipping Modules" in h1)
    driver.find_element_by_css_selector("#doc-payment").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Payment Modules" in h1)
    driver.find_element_by_css_selector("#doc-order_total").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Order Total Modules" in h1)
    driver.find_element_by_css_selector("#doc-order_success").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Order Success Modules" in h1)
    driver.find_element_by_css_selector("#doc-order_action").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Order Action Modules" in h1)
    driver.find_element_by_xpath("//span[.='Orders']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Orders" in h1)
    driver.find_element_by_css_selector("#doc-orders").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Orders" in h1)
    driver.find_element_by_css_selector("#doc-order_statuses").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Order Statuses" in h1)
    driver.find_element_by_xpath("//span[.='Pages']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Pages" in h1)
    driver.find_element_by_xpath("//span[.='Reports']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Monthly Sales" in h1)
    driver.find_element_by_css_selector("#doc-monthly_sales").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Monthly Sales" in h1)
    driver.find_element_by_css_selector("#doc-most_sold_products").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Most Sold Products" in h1)
    driver.find_element_by_css_selector("#doc-most_shopping_customers").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Most Shopping Customers" in h1)
    driver.find_element_by_xpath("//span[.='Settings']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Settings" in h1)
    driver.find_element_by_css_selector("#doc-store_info").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Settings" in h1)
    driver.find_element_by_css_selector("#doc-defaults").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Settings" in h1)
    driver.find_element_by_css_selector("#doc-general").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Settings" in h1)
    driver.find_element_by_css_selector("#doc-listings").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Settings" in h1)
    driver.find_element_by_css_selector("#doc-images").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Settings" in h1)
    driver.find_element_by_css_selector("#doc-checkout").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Settings" in h1)
    driver.find_element_by_css_selector("#doc-advanced").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Settings" in h1)
    driver.find_element_by_css_selector("#doc-security").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Settings" in h1)
    driver.find_element_by_xpath("//span[.='Slides']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Slides" in h1)
    driver.find_element_by_xpath("//span[.='Tax']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Tax Classes" in h1)
    driver.find_element_by_css_selector("#doc-tax_classes").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Tax Classes" in h1)
    driver.find_element_by_css_selector("#doc-tax_rates").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Tax Rates" in h1)
    driver.find_element_by_xpath("//span[.='Translations']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Search Translations" in h1)
    driver.find_element_by_css_selector("#doc-search").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Search Translations" in h1)
    driver.find_element_by_css_selector("#doc-scan").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Scan Files For Translations" in h1)
    driver.find_element_by_css_selector("#doc-csv").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("CSV Import/Export" in h1)
    driver.find_element_by_xpath("//span[.='Users']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("Users" in h1)
    driver.find_element_by_xpath("//span[.='vQmods']").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("vQmods" in h1)
    driver.find_element_by_css_selector("#doc-vqmods").click()
    h1 = driver.find_element_by_css_selector("h1").text
    assert ("vQmods" in h1)