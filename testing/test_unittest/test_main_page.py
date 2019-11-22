from time import sleep
from testing.test_unittest.test_base import BaseSelenium


class BurgerMenuTestCase(BaseSelenium):

    def testing_if_exist_burger_menu(self):
        """testing if exist burger button"""
        self.login()
        sleep(1)
        self.get_burger_button().click()
        drop_down_menu = self.selenium.find_element_by_class_name(
                         'dropdown-menu')
        sleep(1)
        li_all_words = set(drop_down_menu.text.split('\n'))
        set_en = {'My Profile', 'Account Information', 'Reports',
                  'Data Sharing', 'Upload Data', 'Delete All Hydrants',
                  'How-To Videos', 'Logout'}
        sleep(1)
        self.assertEquals(set_en, li_all_words)

    def testing_flow_button(self):
        """testing flow button"""
        self.login()
        sleep(1)
        info_flow_panel = self.selenium.find_element_by_class_name(
            'tab-content')
        set_text = set(info_flow_panel.text.split('\n'))
        set_words = {'Icon Legend', 'Flow Data', 'Hydrant Information',
                     'Dry Hydrant', '1500+ GPM', '1000 to less than 1500 GPM',
                     'Unknown', 'Selected Hydrants: 0',
                     'Total Flow Rate: 0 gal/min', 'No hydrant selected.',
                     '500 to less than 1000 GPM', '0 to less than 500 GPM'}
        sleep(1)
        self.assertEquals(set_words, set_text)

    def testing_location_button(self):
        """testing location button"""
        self.login()
        sleep(3)
        self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/ul/li[2]').click()
        sleep(1)
        info_location_panel = self.selenium.find_element_by_xpath(
            '//*[@id="info-tabs-pane-2"]')
        sleep(3)
        set_text = set(info_location_panel.text.split('\n'))
        set_words = {'Location Data', 'Flow Data', 'Hydrant Information',
                     'Selected Hydrants: 0', 'No location selected.',
                     'Total Flow Rate: 0 gal/min', 'No hydrant selected.'}
        sleep(1)
        self.assertEquals(set_words, set_text)

    def testing_building_data_button(self):
        """testing building button"""
        self.login()
        sleep(3)
        self.selenium.find_element_by_xpath(
            '//*[@id="info-tabs-tab-3"]').click()
        sleep(1)
        info_building_panel = self.selenium.find_element_by_id(
            'info-tabs-pane-3')
        set_text = set(info_building_panel.text.split('\n'))
        set_words = {'Building Data', 'No building info.'}
        sleep(1)
        self.assertEquals(set_words, set_text)

    def testing_dispatch_button(self):
        """testing dispatch button"""
        self.login()
        sleep(3)
        self.selenium.find_element_by_xpath(
            '//*[@id="info-tabs-tab-4"]').click()
        sleep(1)
        info_dispatch_panel = self.selenium.find_element_by_id(
            'info-tabs-pane-4')
        set_text = set(info_dispatch_panel.text.split('\n'))
        set_words = {'No Messages.'}
        sleep(1)
        self.assertEquals(set_words, set_text)
