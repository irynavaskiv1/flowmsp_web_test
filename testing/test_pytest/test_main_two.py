import pytest
from time import sleep
from constants import LOGIN, PASSWORD


@pytest.fixture()
def test_if_login_works(self):
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

    get_info_tabs = self.selenium.find_element_by_xpath(
        '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/ul')
    set_get_info_tabs = set(get_info_tabs.text.split('\n'))
    set_words = {'Flow', 'Location'}
    assert set_words in set_get_info_tabs
