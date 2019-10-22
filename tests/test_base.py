import unittest
from time import sleep
from selenium import webdriver
from constants import LOGIN, PASSWORD


class BaseSelenium(unittest.TestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.get(
            '{}{}'.format('https://app.flowmsp.com', '/login'))
        sleep(2)

    def login(self):
        username_field = self.selenium.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/'
            'form/div[1]/input')
        username_field.send_keys(LOGIN)
        sleep(3)

        password_field = self.selenium.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/'
            'form/div[2]/input')
        password_field.send_keys(PASSWORD)
        sleep(3)

        login_button = self.selenium.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/'
            'form/div[3]/input')
        login_button.click()
        sleep(3)

    def get_burger_button(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/nav/div/div/div[2]/ul/li/a/span[1]/i')

    def get_navigation_drawer_button(self):
        return self.selenium.find_element_by_id('basic-nav-dropdown')

    def get_my_profile_button(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/nav/div/div/div[2]/ul/li/ul/li[1]/a')

    def tearDown(self):
        self.selenium.close()


if __name__ == '__main__':
    unittest.main()


class MyProfileBaseTestCase(BaseSelenium):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.get(
            '{}{}'.format('https://app.flowmsp.com', '/login'))
        sleep(2)

    def login_to_profile(self):
        self.login()
        sleep(2)
        self.get_burger_button().click()
        sleep(2)
        self.get_my_profile_button().click()
        sleep(2)

    def get_edit_profile_button(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/button[1]')

    def get_change_password_button(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/button[2]')

    def tearDown(self):
        self.selenium.close()


class FilerBaseTestCase(BaseSelenium):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.get(
            '{}{}'.format('https://app.flowmsp.com', '/login'))
        sleep(2)

    def login_to_filer_block(self):
        self.login()
        sleep(2)
        filter_button = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/span[1]')
        filter_button.click()

    def get_filter_block(self):
        return self.selenium.find_element_by_class_name('form-horizontal')

    def get_back_button(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/'
            'div[2]/form/div[1]/span')

    def tearDown(self):
        self.selenium.close()


class AccountInfoBaseTestCase(BaseSelenium):

    def get_account_info_button(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/nav/div/div/div[2]/ul/li/ul/li[2]')

    def get_edit_account_info_button(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/button[1]')

    def login_to_account_info_block(self):
        self.login()
        self.get_navigation_drawer_button().click()
        self.get_account_info_button().click()
        sleep(1)


class UploadDataBaseTestCase(BaseSelenium):

    def get_upload_data_button(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div/div/nav/div/div/div[2]/ul/li/ul/li[5]/a')

    def login_to_upload_data(self):
        self.login()
        self.get_navigation_drawer_button()
        self.get_upload_data_button()
        sleep(1)
