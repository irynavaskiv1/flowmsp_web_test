from tests_pytest.test_base_pytest import BaseSelenium


class MainPageTestCase(BaseSelenium):

    def test_if_login_works(self):
        self.login()
        self.assertTrue()
