from time import sleep
from tests.test_base import FilerBaseTestCase


class FilterTestCase(FilerBaseTestCase):

    def testing_if_filter_exist(self):
        """testing if exist filter button"""
        self.login_to_filer_block()
        self.get_filter_block()
        set_text = set(self.get_filter_block().text.split('\n'))
        set_words = {'Partner preference', 'Building Info.', 'Buildings',
                     'Buildings with..', 'Structures', 'Pre-plans',
                     'Area(sq.ft.)', 'Clear', 'Sprinklered', 'Multi-family',
                     'Exclude Partner', 'Select Pre-plans', 'Vacant',
                     'Present', 'Standpipes', 'Within the Last 30 Days',
                     'Special', 'Older than a year', 'Apply', 'Fire Alarms',
                     'Commercial', 'Non-sprinklered', 'Not present',
                     'Select Building Info Option', 'Without pictures',
                     'Truss Roof', 'With pictures'}
        sleep(2)
        self.assertEquals(set_words, set_text)

    def testing_if_apply_and_clear_buttons_exist(self):
        """testing if exist apply button"""
        self.login_to_filer_block()
        filter_block = self.selenium.find_element_by_class_name(
            'form-group')
        set_text = set(filter_block.text.split('\n'))
        set_words = {'Apply', 'Clear'}
        sleep(1)
        self.assertEquals(set_words, set_text)

    def testing_if_work_back_button(self):
        """testing if back button hide page"""
        self.login_to_filer_block()
        self.get_filter_block()
        set_text = set(self.get_filter_block().text.split('\n'))
        set_words = {'Partner preference', 'Building Info.', 'Buildings',
                     'Buildings with..', 'Structures', 'Pre-plans'}
        sleep(2)
        self.get_back_button().click()
        self.assertNotIn(set_words, set_text)
