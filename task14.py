import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def testWindows(driver):
    wait = WebDriverWait(driver, 5)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    username = driver.find_element_by_name("username").send_keys("admin")
    password = driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    #go inside edit country page
    driver.find_element_by_xpath("//a[.='Afghanistan']").click()

    #open new windows and close them
    # windows_before = driver.window_handles[0]
    # driver.find_element_by_css_selector("[href='http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2']").click()
    # windows_after = driver.window_handles[1]
    # WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) == 2)
    # driver.switch_to_window(windows_after)
    # driver.close()
    # driver.switch_to_window(windows_before)

    # open new windows and close them
    windows_before = driver.current_window_handle
    driver.find_element_by_css_selector("[href='http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2']").click()
    windows_after = driver.window_handles
    new_window = [x for x in windows_after if x != windows_before][0]
    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) == 2)
    driver.switch_to_window(new_window)
    driver.close()
    driver.switch_to_window(windows_before)

    windows_before = driver.current_window_handle
    driver.find_element_by_css_selector('[href="http://en.wikipedia.org/wiki/ISO_3166-1_alpha-3"]').click()
    windows_after = driver.window_handles
    new_window = [x for x in windows_after if x != windows_before][0]
    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) == 2)
    driver.switch_to_window(new_window)
    driver.close()
    driver.switch_to_window(windows_before)

    windows_before = driver.current_window_handle
    driver.find_element_by_css_selector('[href="https://en.wikipedia.org/wiki/Regular_expression"]').click()
    windows_after = driver.window_handles
    new_window = [x for x in windows_after if x != windows_before][0]
    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) == 2)
    driver.switch_to_window(new_window)
    driver.close()
    driver.switch_to_window(windows_before)

    windows_before = driver.current_window_handle
    driver.find_element_by_css_selector\
        ('[href="http://www.addressdoctor.com/en/countries-data/address-formats.html"]').click()
    windows_after = driver.window_handles
    new_window = [x for x in windows_after if x != windows_before][0]
    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) == 2)
    driver.switch_to_window(new_window)
    driver.close()
    driver.switch_to_window(windows_before)

    windows_before = driver.current_window_handle
    driver.find_element_by_css_selector('[href="https://en.wikipedia.org/wiki/Regular_expression"]').click()
    windows_after = driver.window_handles
    new_window = [x for x in windows_after if x != windows_before][0]
    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) == 2)
    driver.switch_to_window(new_window)
    driver.close()
    driver.switch_to_window(windows_before)

    windows_before = driver.current_window_handle
    driver.find_element_by_css_selector('[href="https://en.wikipedia.org/wiki/List_of_countries_'
                                        'and_capitals_with_currency_and_language"]').click()
    windows_after = driver.window_handles
    new_window = [x for x in windows_after if x != windows_before][0]
    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) == 2)
    driver.switch_to_window(new_window)
    driver.close()
    driver.switch_to_window(windows_before)

    windows_before = driver.current_window_handle
    driver.find_element_by_css_selector('[href="https://en.wikipedia.org/wiki/List_of_country_calling_codes"]').click()
    windows_after = driver.window_handles
    new_window = [x for x in windows_after if x != windows_before][0]
    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) == 2)
    driver.switch_to_window(new_window)
    driver.close()
    driver.switch_to_window(windows_before)
















