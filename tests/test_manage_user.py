import time

import pytest

from config.TestDataMy import TestData as TD
from pages.LoginPage import LoginPage
from pages.ManageUserPage import ManageUserPage
from pages.PeoplePage import PeoplePage, URLLocators


class TestManageUserPage:

    def get_element_from_people_page(self, locator):
        driver = PeoplePage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE)
        lst = driver.get_elements_text(locator)
        return lst

    def login_with_default_credential(self):
        driver = LoginPage(self.driver)
        driver.login_jenkins(TD.LOGIN, TD.PASSWORD)

    def test_create_user_valid_credential(self):
        """
        TC_JN_35
        create user with valid credentials
        verify, that user present on the page
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save(ManageUserPage.USER_NAME, ManageUserPage.PASSWORD)

        assert driver.get_current_url() == ManageUserPage.URL_USER_MANAGE
        assert driver.get_elements_text(ManageUserPage.USER_ID)[0] == ManageUserPage.USER_NAME

    def test_added_new_user_on_the_people_page(self):
        """
        TC_JN_37
        verify that on the PeoplePage new record in the list
        :return:
        """
        driver = PeoplePage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE)
        lst = driver.get_elements_text(ManageUserPage.PEOPLE_LIST)
        assert lst[1] == ManageUserPage.USER_NAME
        lst.clear()

    def test_check_log_in_new_user(self):
        """
        TC_JN_36
        verify that we can login with login/password new user
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click(ManageUserPage.LOG_OUT_BUTTON)
        driver = LoginPage(self.driver)
        driver.login_jenkins(ManageUserPage.USER_NAME, ManageUserPage.PASSWORD)

        assert driver.get_current_url() == TD.BASE_URL

    def test_delete_new_user(self):
        """
        TC_JN_38
        verify, that user present on the page
        verify, that user was deleted
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.click(ManageUserPage.LOG_OUT_BUTTON)
        self.login_with_default_credential()
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)

        assert driver.is_element_present(ManageUserPage.USER_ID)

        driver.click(ManageUserPage.USER_ID_DELETE)
        driver.click(ManageUserPage.USER_ID_YES)

        assert driver.is_element_not_present(ManageUserPage.USER_ID)

    def test_deleted_new_user_on_the_people_page(self):
        """
        TC_JN_40
        verify that on the PeoplePage new record is not in the list
        :return:
        """

        lst = self.get_element_from_people_page(ManageUserPage.PEOPLE_LIST_ALL_RECORD)
        assert ManageUserPage.USER_NAME is not lst
        lst.clear()

    def test_verify_cant_log_in_new_user_after_deleted(self):
        """
        TC_JN_39
        verify that we can't login with deleted login/password new user
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click(ManageUserPage.LOG_OUT_BUTTON)
        driver = LoginPage(self.driver)
        driver.login_jenkins(ManageUserPage.USER_NAME, ManageUserPage.PASSWORD)

        assert driver.get_current_url() == LoginPage.URL_LOGIN_ERROR
        assert driver.get_element_text(LoginPage.ALERT_INVALID_DATA) == LoginPage.ALERT_TEXT

    @pytest.mark.skip
    def test_create_user_with_underscore_name(self):
        """
        TC_JN_64
        create user with '_' name
        verify, that user present on the page
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save(ManageUserPage.USER_NAME_UNDERSCORE, ManageUserPage.PASSWORD)

        assert driver.get_elements_text(ManageUserPage.USER_ID_UNDERSCORE)[0] == ManageUserPage.USER_NAME_UNDERSCORE
        self.test_delete_new_user()

    @pytest.mark.skip
    def test_create_user_with_hyphen_name(self):
        """
        TC_JN_72
        create user with '-' name
        verify, that user present on the page
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save(ManageUserPage.USER_NAME_HYPHEN, ManageUserPage.PASSWORD)

        assert driver.get_elements_text(ManageUserPage.USER_ID_HYPHEN)[0] == ManageUserPage.USER_NAME_HYPHEN

    @pytest.mark.skip
    def test_create_user_with_long_name(self):
        """
        TC_JN_79
        create user with name more than 255 ch
        verify, that user present on the page
        :return:
        """
        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save(ManageUserPage.USER_NAME_MORE_255_SYMBOLS, ManageUserPage.PASSWORD)

        assert driver.get_elements_text(ManageUserPage.USER_ID_MORE_255_SYMBOLS)[0] \
               == ManageUserPage.USER_NAME_MORE_255_SYMBOLS

    def test_edit_new_user_fullname(self):
        """
        TC_JN_41
        verify that we can change fullname
        :return:
        """
        self.login_with_default_credential()
        self.test_create_user_valid_credential()

        lst = self.get_element_from_people_page(ManageUserPage.PEOPLE_LIST)
        assert lst[1] == ManageUserPage.USER_NAME
        assert lst[2] == ManageUserPage.USER_FULLNAME
        lst.clear()

        driver = ManageUserPage(self.driver)
        driver.go_to_page(ManageUserPage.URL_USER_MANAGE)
        driver.click(ManageUserPage.CONFIGURE_USER)

        driver.clear(ManageUserPage.INPUT_FULLNAME)
        driver.do_send_keys(ManageUserPage.INPUT_FULLNAME, ManageUserPage.USER_FULLNAME_EDIT)
        driver.clear(ManageUserPage.INPUT_EMAIL)
        driver.do_send_keys(ManageUserPage.INPUT_EMAIL, ManageUserPage.USER_EMAIL_EDIT)
        driver.clear(ManageUserPage.INPUT_PASSWORD)
        driver.do_send_keys(ManageUserPage.INPUT_PASSWORD, ManageUserPage.PASSWORD_EDIT)
        driver.clear(ManageUserPage.INPUT_CONFIRM_PASSWORD)
        driver.do_send_keys(ManageUserPage.INPUT_CONFIRM_PASSWORD, ManageUserPage.PASSWORD_EDIT)

        driver.click(ManageUserPage.USER_ID_YES)
        driver.get_element(ManageUserPage.SAVE_BUTTON).click()

        lst = self.get_element_from_people_page(ManageUserPage.PEOPLE_LIST)
        assert lst[1] == ManageUserPage.USER_NAME
        assert lst[2] == ManageUserPage.USER_FULLNAME_EDIT
        lst.clear()

        self.test_delete_new_user()
