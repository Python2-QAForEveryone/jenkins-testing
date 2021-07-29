import pytest

from pages.LoginPage import LoginPageLocators, LoginPage
from pages.ManageUserPage import ManageUserPage


class TestManageUserPage:

    def test_create_user_valid_credential(self):
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save()
        assert driver.get_current_url() == ManageUserPage.URL_USER_MANAGE
        assert driver.get_elements_text(ManageUserPage.USER_ID)[0] == ManageUserPage.USER_NAME

    def test_check_log_in_new_user(self):
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click(ManageUserPage.LOG_OUT_BUTTON)
        driver.do_send_keys(LoginPageLocators.INPUT_LOGIN, ManageUserPage.name)
        # DON'T WORK+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # driver.do_send_keys(LoginPageLocators.INPUT_PASSWORD, ManageUserPage.password)
        driver.click(LoginPageLocators.SIGN_IN_BUTTON)



