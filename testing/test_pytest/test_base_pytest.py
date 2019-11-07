import pytest

from time import sleep

from _pytest import unittest
from selenium.webdriver.firefox import webdriver
from constants import LOGIN, PASSWORD


class BaseSelenium(unittest.TestCaseFunction):
    sleep_time = 0.5

    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.get(
            '{}{}'.format('https://app.flowmsp.com', '/login'))
        sleep(self.sleep_time)

    def login(self):
        username_field = self.selenium.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/'
            'form/div[1]/input')
        username_field.send_keys(LOGIN)
        sleep(self.sleep_time)

        password_field = self.selenium.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/'
            'form/div[2]/input')
        password_field.send_keys(PASSWORD)
        sleep(self.sleep_time)

        login_button = self.selenium.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/'
            'form/div[3]/input')
        login_button.click()
        sleep(self.sleep_time)

    def test_if_login_works(self):
        self.login()
        get_info_tabs = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/ul')
        set_get_info_tabs = set(get_info_tabs.text.split('\n'))
        set_words = {'Flow', 'Location'}
        assert set_words in set_get_info_tabs

    def tearDown(self):
        self.selenium.close()
