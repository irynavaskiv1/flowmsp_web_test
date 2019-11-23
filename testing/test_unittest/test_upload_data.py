from time import sleep
from testing.test_unittest.test_base import UploadDataBaseTestCase


class UploadDataTestCase(UploadDataBaseTestCase):
    """ testing upload data inside burger menu"""

    def testing_all_pages(self):
        self.login_to_upload_data()
        all_page = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]')
        set_text = set(all_page.text.split('\n'))
        sleep(1)
        set_words = {'Upload Data', 'Hydrants', 'Preplans', 'Users', 'Upload',
                     '[*Select an option and choose the file to upload]'}
        self.assertEquals(set_words, set_text)
