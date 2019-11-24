from time import sleep
from testing.test_unittest.test_base import DataSharingBaseTestCase


class DataSharingTestCase(DataSharingBaseTestCase):

    def test_if_all_words_exist(self):
        """testing if all words exist"""
        self.login_to_data_sharing()
        sleep(3)
        text_inside_page = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]')
        li_all_words = set(text_inside_page.text.split('\n'))
        set_en = {'I agree to share preplanning data with other fire departments.',
                  'Radius', 'In MilesSearch Partners',
                  'No matching records found.'}
        sleep(1)
        self.assertEquals(set_en, li_all_words)
