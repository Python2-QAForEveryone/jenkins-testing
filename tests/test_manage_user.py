import pytest

from pages.ManageUserPage import ManageUserPage


class TestManageUserPage:

    def test_create_new_user(self):
        driver = ManageUserPage.go_to_manage_user_page(self)
        driver.click_button_create_new_user()
        driver.fill_all_field_and_click_save()
        driver.click(ManageUserPage.USER_ID)
        # assert driver.get_current_url() == ManageUserPage.URL_USER_MANAGE
        # assert driver.get_element_text(ManageUserPage.USER_ID) == ManageUserPage.USER_NAME
