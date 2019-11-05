from time import sleep

from testing.tests import UploadDataBaseTestCase


class UploadDataTestCase(UploadDataBaseTestCase):

    def testing_all_pages(self):
        self.login_to_upload_data()
        all_page = self.selenium.find_element_by_xpath(
            '/html/body/div/div/div')
        set_text = set(all_page.text.split('\n'))
        sleep(1)
        set_words = {'Dispatch', 'Location',  'Satellite', 'Icon Legend',
                     'Pre-plans183No. of Hydrants292', 'No hydrant selected.',
                     '0 to less than 500 GPM', '1000 to less than 1500 GPM',
                     'Unknown', '1500+ GPM', 'Map',
                     'Unknown', '1500+ GPM', 'Map', 'Flow Data', 'Flow',
                     'Map data ©2019 Google Imagery ©2019 CNES / Airbus, '
                     'European Space Imaging, Maxar Technologies',
                     'Building Data', 'Total Flow Rate: 0 gal/min',
                     'Terms of Use', 'sffec354fvf35', 'Dry Hydrant',
                     '500 to less than 1000 GPM', 'Selected Hydrants: 0',
                     'Location', 'Hydrant Information'}
        self.assertEquals(set_words, set_text)
