import time

import pytest

from config.TestDataMy import TestData as TD
from pages.LoginPage import LoginPage
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
        driver = LoginPage(self.driver)
        driver.login_jenkins(ManageUserPage.name, ManageUserPage.password)

        assert driver.get_current_url() == TD.BASE_URL


    def test_delete_new_user(self):
        LoginPage.login_jenkins(TD.LOGIN, TD.PASSWORD)
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        time.sleep(2)
        driver.click(ManageUserPage.USER_ID_DELETE)
        driver.click(ManageUserPage.USER_ID_DELETE_YES)
        time.sleep(2)
