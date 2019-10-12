import os
import unittest
import time
from selenium import webdriver

from constants import password, login


class BaseSelenium(unittest.TestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.get("https://app.flowmsp.com/login")
        time.sleep(2)

    def login(self):
        username_field = self.selenium.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/'
            'form/div[1]/input')
        username_field.send_keys(login)
        time.sleep(3)

        password_field = self.selenium.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/'
            'form/div[2]/input')
        password_field.send_keys(password)
        time.sleep(3)

        login_button = self.selenium.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/'
            'form/div[3]/input')
        login_button.click()
        time.sleep(3)

    def tearDown(self):
        self.selenium.close()


if __name__ == '__main__':
    unittest.main()

