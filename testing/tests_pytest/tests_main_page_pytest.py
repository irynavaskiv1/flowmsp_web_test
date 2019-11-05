from testing.tests_pytest.tests_base_pytest import BaseSelenium


class MainPageTestCase(BaseSelenium):

    def test_if_login_works(self):
        self.login()
        get_info_tabs = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/ul')
        set_get_info_tabs = set(self.get_info_tabs.text.split('\n'))
        set_words = {'Flow', 'Location'}
        assert set_words in set_get_info_tabs
