from tests.test_base import MyProfileBaseTestCase
import time


class MyProfileTestCase(MyProfileBaseTestCase):

    def testing_my_profile_page(self):
        """testing if profile page has all fields"""
        self.login_to_profile()
        time.sleep(3)
        all_page_text = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]')
        time.sleep(3)
        set_text = set(all_page_text.text.split('\n'))
        set_words = {'Customer Name:', 'First Name:', 'Last Name:', 'Email:'
                     'Role:'}
        time.sleep(3)
        self.assertEquals(set_words, set_text)

    def testing_edit_profile_button(self):
        """testing if exist edit page"""
        self.login_to_profile()
        self.get_my_profile_button().click()
        edit_page_alert = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/button[1]')
        time.sleep(2)
        set_text = set(edit_page_alert.text.split('\n'))
        set_words = {'Edit My Profile', 'First Name', 'Last Name', 'Submit'}
        time.sleep(3)
        self.assertEquals(set_words, set_text)

    def testing_change_password_button(self):
        """testing if exist change password page"""
        self.login_to_profile()
        self.get_change_password_buttton()
        change_password_alert = self.selenium.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div')
        time.sleep(2)
        set_text = set(change_password_alert.text.split('\n'))
        set_words = {'Change Password', 'Current Password', 'New Password',
                     'Confirm New Password', 'Submit'}
        time.sleep(2)
        self.assertEquals(set_words, set_text)

