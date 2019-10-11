import time
from project.test_base import BaseSelenium


class BurgerMenuTestCase(BaseSelenium):

    def testing_if_exist_burger_menu(self):
        """тестуємо чи є бургер меню кнопка"""
        self.login()
        time.sleep(2)
        burger_button = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/nav/div/div/div[2]/ul/li/a/span[1]/i')
        burger_button.click()
        drop_down_menu = self.selenium.find_element_by_class_name(
                         'dropdown-menu')
        time.sleep(2)
        li_all_words = set(drop_down_menu.text.split('\n'))
        set_en = {'My Profile', 'Account Information', 'Reports',
                  'Data Sharing', 'Upload Data', 'Delete All Hydrants',
                  'How-To Videos', 'Logout'}
        time.sleep(2)
        self.assertEquals(set_en, li_all_words)

    def testing_flow_button(self):
        """тестуємо flow кнопку"""
        self.login()
        flow_button = self.selenium.find_element_by_id('info-tabs-tab-1')
        flow_button.click()
        time.sleep(2)
        info_flow_panel = self.selenium.find_element_by_id('info-pane-1')
        set_text = set(info_flow_panel.text.split('\n'))
        set_words = {'Icon Legend', 'Flow Data', 'Hydrant Information'}
        time.sleep(3)
        self.assertEquals(set_words, set_text)

    def testing_location_menu(self):
        """тестуємо location кнопку"""
        self.login()
        location_button = self.selenium.find_element_by_id('info-tabs-tab-2')
        location_button.click()
        time.sleep(2)
        info_location_panel = self.selenium.find_element_by_id(
            'info-tabs-pane-2')
        set_text = set(info_location_panel.text.split('\n'))
        set_words = {'Location Data', 'Flow Data', 'Hydrant Information'}
        time.sleep(3)
        self.assertEquals(set_words, set_text)

    def testing_building_data(self):
        """тестуємо building кнопку"""
        self.login()
        building_data_button = self.selenium.find_element_by_id(
            'info-tabs-tab-3')
        building_data_button.click()
        time.sleep(2)
        info_building_panel = self.selenium.find_element_by_id(
            'info-tabs-pane-3')
        set_text = set(info_building_panel.text.split('\n'))
        set_words = {'Building Data'}
        time.sleep(3)
        self.assertEquals(set_words, set_text)


class SearchTestCase(BaseSelenium):

    def testing_if_search_exist(self):
        self.login()
        time.sleep(2)
        search_field = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/div/div[1]'
            '/div/div/input')
        search_field.send_keys('Lviv')


class FilterTestCase(BaseSelenium):

    def testing_if_filter_exist(self):
        """тестуємо чи є filter кнопка"""
        self.login()
        time.sleep(2)
        filter_button = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/span[1]')
        filter_button.click()
        filter_block = self.selenium.find_element_by_class_name(
            'form-horizontal')
        set_text = {filter_block.text.split('\n')}
        set_words = {'Partner preference', 'Building Info.', 'Buildings',
                     'Buildings with..', 'Structures', 'Pre-plans',
                     'Area(sq.ft.)'}
        time.sleep(3)
        self.assertEquals(set_words, set_text)

    def testing_if_apply_and_clear_exist(self):
        """тестуємо чи є apply кнопка"""
        self.login()
        time.sleep(2)
        filter_button = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/span[1]')
        filter_button.click()
        filter_block = self.selenium.find_element_by_class_name(
            'form-group')
        set_text = {filter_block.text.split('\n')}
        set_words = {'Apply', 'Clear'}
        time.sleep(3)
        self.assertEquals(set_words, set_text)

