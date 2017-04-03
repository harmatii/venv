# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
import unittest
from selenium.webdriver.common.by import By
from is_present import ispresent
from selenium.webdriver.common.keys import Keys


class hrm(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()

    def test_hrm(self):
        driver = self.driver
        driver.get("http://hrm.seleniumminutes.com/")
        username = driver.find_element_by_css_selector("#txtUsername")
        username.clear()
        username.send_keys("Admin")
        password = driver.find_element_by_css_selector("#txtPassword")
        password.clear()
        password.send_keys("Password")
        login = driver.find_element_by_css_selector("#btnLogin")
        login.click()
        welcome = driver.find_element_by_css_selector("#welcome")
        welcome.get_attribute("textContent")
        print(welcome)






    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.driver.quit()
