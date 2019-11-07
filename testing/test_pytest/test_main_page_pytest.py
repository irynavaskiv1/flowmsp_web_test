from testing.test_pytest.test_base_pytest import BaseSelenium


class MainPageTestCase(BaseSelenium):

    def test_if_login_works(self):
        self.login()
        get_info_tabs = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/ul')
        set_get_info_tabs = set(get_info_tabs.text.split('\n'))
        set_words = {'Flow', 'Location'}
        assert set_words in set_get_info_tabs


class TestClass:

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
