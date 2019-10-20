from tests.test_base import MyProfileBaseTestCase
from time import sleep


class MyProfileTestCase(MyProfileBaseTestCase):

    def test_exist_my_profile_page(self):
        """testing if profile page has all fields"""
        self.login_to_profile()
        all_page_text = self.selenium.find_element_by_class_name(
            'main-container')
        sleep(1)
        set_text = set(all_page_text.text.split('\n'))
        set_words = {'First Name:', 'Last Name:', 'Role:', 'Customer Name:',
                     'ADMIN', 'Pre-plans183No. of Hydrants292', 'My Profile',
                     'Email:', 'aa@aa.aa', 'Edit ProfileChange Password',
                     'aaaaaa'}
        sleep(1)
        self.assertEquals(set_words, set_text)

    def test_existing_edit_profile_button(self):
        """testing if exist edit page"""
        self.login_to_profile()
        self.get_edit_profile_button().click()
        edit_page_alert = self.selenium.find_element_by_class_name(
            'modal-dialog')
        sleep(1)
        set_text = set(edit_page_alert.text.split('\n'))
        set_words = {'Edit My Profile', 'First Name*', 'Last Name*', '×',
                     'Submit', 'Close'}
        sleep(1)
        self.assertEquals(set_words, set_text)

    def testing_change_password_button(self):
        """testing if exist change password page"""
        self.login_to_profile()
        self.get_change_password_button().click()
        sleep(3)
        change_password_alert = self.selenium.find_element_by_class_name(
            'modal-dialog')
        sleep(3)
        set_text = set(change_password_alert.text.split('\n'))
        set_words = {'Current Password*', 'Change Password', 'Close', '×',
                     'Confirm New Password*', 'Submit', 'New Password*'}
        sleep(3)
        self.assertEquals(set_text, set_words)
