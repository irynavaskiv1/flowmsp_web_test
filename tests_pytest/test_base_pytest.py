import pytest

from time import sleep
from constants import LOGIN, PASSWORD


class BaseSelenium:
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

    def tearDown(self):
        self.selenium.close()

