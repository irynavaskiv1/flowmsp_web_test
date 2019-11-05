<<<<<<< HEAD:testing/test_pytest/test_main_page_pytest.py
from testing.test_pytest.test_base_pytest import BaseSelenium
=======
from testing.tests_pytest.tests_base_pytest import BaseSelenium
>>>>>>> fe5d25ce50126d084f5a86290e3e95b1c1acf8ee:testing/tests_pytest/tests_main_page_pytest.py


class MainPageTestCase(BaseSelenium):

    def test_if_login_works(self):
        self.login()
        get_info_tabs = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/ul')
        set_get_info_tabs = set(get_info_tabs.text.split('\n'))
        set_words = {'Flow', 'Location'}
        assert set_words in set_get_info_tabs
