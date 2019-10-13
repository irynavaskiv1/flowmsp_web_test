import time

from selenium.webdriver.common.keys import Keys

from tests.test_base import BaseSelenium
# import ipdb; ipdb.set_trace()


class BurgerMenuTestCase(BaseSelenium):

    def testing_if_exist_burger_menu(self):
        """testing if exist burger button"""
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
        """testing flow button"""
        self.login()
        flow_button = self.selenium.find_element_by_id('info-tabs-tab-1')
        flow_button.click()
        time.sleep(2)
        info_flow_panel = self.selenium.find_element_by_class_name(
            'tab-content')
        set_text = set(info_flow_panel.text.split('\n'))
        set_words = {'Icon Legend', 'Flow Data', 'Hydrant Information',
                     'Dry Hydrant', '1500+ GPM', '1000 to less than 1500 GPM',
                     'Unknown', 'Selected Hydrants: 0',
                     'Total Flow Rate: 0 gal/min', 'No hydrant selected.',
                     '500 to less than 1000 GPM', '0 to less than 500 GPM'}
        time.sleep(3)
        self.assertEquals(set_words, set_text)

    def testing_location_button(self):
        """testing location button"""
        self.login()
        location_button = self.selenium.find_element_by_id('info-tabs-tab-2')
        location_button.click()
        time.sleep(2)
        info_location_panel = self.selenium.find_element_by_id(
            'info-tabs-pane-2')
        set_text = set(info_location_panel.text.split('\n'))
        set_words = {'Location Data', 'Flow Data', 'Hydrant Information',
                     'Selected Hydrants: 0', 'No location selected.',
                     'Total Flow Rate: 0 gal/min', 'No hydrant selected.'}
        time.sleep(3)
        self.assertEquals(set_words, set_text)

    def testing_building_data_button(self):
        """testing building button"""
        self.login()
        building_data_button = self.selenium.find_element_by_id(
            'info-tabs-tab-3')
        building_data_button.click()
        time.sleep(2)
        info_building_panel = self.selenium.find_element_by_id(
            'info-tabs-pane-3')
        set_text = set(info_building_panel.text.split('\n'))
        set_words = {'Building Data', 'No building info.'}
        time.sleep(3)
        self.assertEquals(set_words, set_text)

    def testing_dispatch_button(self):
        self.login()
        dispatch_button = self.selenium.find_element_by_id(
            'info-tabs-tab-4')
        dispatch_button.click()
        time.sleep(2)
        info_dispatch_panel = self.selenium.find_element_by_id(
            'info-tabs-pane-4')
        set_text = set(info_dispatch_panel.text.split('\n'))
        set_words = {'No Messages.'}
        time.sleep(3)
        self.assertEquals(set_words, set_text)


class FilterTestCase(BaseSelenium):

    def testing_if_filter_exist(self):
        """testing if exist filter button"""
        self.login()
        time.sleep(2)
        filter_button = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/span[1]')
        filter_button.click()
        filter_block = self.selenium.find_element_by_class_name(
            'form-horizontal')
        set_text = set(filter_block.text.split('\n'))
        set_words = {'Partner preference', 'Building Info.', 'Buildings',
                     'Buildings with..', 'Structures', 'Pre-plans',
                     'Area(sq.ft.)', 'Clear', 'Sprinklered', 'Multi-family',
                     'Exclude Partner', 'Select Pre-plans', 'Vacant',
                     'Present', 'Standpipes', 'Within the Last 30 Days',
                     'Special', 'Older than a year', 'Apply', 'Fire Alarms',
                     'Commercial', 'Non-sprinklered', 'Not present',
                     'Select Building Info Option', 'Without pictures',
                     'Truss Roof', 'With pictures'}
        time.sleep(3)
        self.assertEquals(set_words, set_text)

    def testing_if_apply_and_clear_exist(self):
        """testing if exist apply button"""
        self.login()
        time.sleep(2)
        filter_button = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/span[1]')
        filter_button.click()
        filter_block = self.selenium.find_element_by_class_name(
            'form-group')
        set_text = set(filter_block.text.split('\n'))
        set_words = {'Apply', 'Clear'}
        time.sleep(3)
        self.assertEquals(set_words, set_text)
