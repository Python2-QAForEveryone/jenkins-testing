from pages.FolderPage import FolderPage
from pages.FolderPage import FolderPageLocator


class TestFolderPage:

    def test_create_folder(self):
        driver = FolderPage(self.driver)
        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        driver.get_element(FolderPageLocator.OK_BUTTON).click()
        assert driver.get_title() == FolderPage.TITLE
        driver.get_wait(FolderPageLocator.SAVE_BUTTON)
        driver.get_element(FolderPageLocator.SAVE_BUTTON).click()
        assert driver.get_title() == FolderPage.TITLE_JOB
        driver.get_element(FolderPageLocator.LINK_DELETE_FOLDER).click()
        driver.get_element(FolderPageLocator.BUTTON_YES).click()

    def test_name_folder_more_255_ch(self):
        driver = FolderPage(self.driver)
        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.long_name)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        driver.get_element(FolderPageLocator.OK_BUTTON).click()
        assert driver.get_title() == FolderPage.WRONG_TITLE
        assert driver.is_element_present(FolderPageLocator.WRONG_REQUEST)

    def test_name_folder_start_special_ch(self):
        driver = FolderPage(self.driver)
        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name_start_special_ch)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        assert driver.is_element_present(FolderPageLocator.OK_BUTTON_DISABLED)
        assert driver.is_element_present(FolderPageLocator.ITEM_NAME_INVALID)

    def test_name_folder_inside_special_ch(self):
        driver = FolderPage(self.driver)
        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name_inside_special_ch)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        assert driver.is_element_present(FolderPageLocator.ITEM_NAME_INVALID)
        driver.get_element(FolderPageLocator.OK_BUTTON).click()
        assert driver.is_element_present(FolderPageLocator.ERROR_PAGE)

    def test_name_folder_digits(self):
        driver = FolderPage(self.driver)
        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name_digits)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        driver.get_element(FolderPageLocator.OK_BUTTON).click()
        assert driver.get_title() == FolderPage.TITLE_DIGITS
        driver.get_wait(FolderPageLocator.SAVE_BUTTON)
        driver.get_element(FolderPageLocator.SAVE_BUTTON).click()
        assert driver.get_title() == FolderPage.TITLE_DIGITS_JOB
        driver.get_element(FolderPageLocator.LINK_DELETE_FOLDER).click()
        driver.get_element(FolderPageLocator.BUTTON_YES).click()

    def test_name_folder_empty(self):
        driver = FolderPage(self.driver)
        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name_empty)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        assert driver.is_element_present(FolderPageLocator.OK_BUTTON_DISABLED)
        assert driver.is_element_present(FolderPageLocator.ITEM_NAME_REQUIRED)

    def test_name_folder_start_dot(self):
        driver = FolderPage(self.driver)
        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name_start_dot)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        driver.get_element(FolderPageLocator.OK_BUTTON).click()
        assert driver.get_title() == FolderPage.TITLE_START_DOT
        driver.get_wait(FolderPageLocator.SAVE_BUTTON)
        driver.get_element(FolderPageLocator.SAVE_BUTTON).click()
        assert driver.get_title() == FolderPage.TITLE_START_DOT_JOB
        driver.get_element(FolderPageLocator.LINK_DELETE_FOLDER).click()
        driver.get_element(FolderPageLocator.BUTTON_YES).click()

    def test_name_folder_inside_dot(self):
        driver = FolderPage(self.driver)
        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name_inside_dot)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        driver.get_element(FolderPageLocator.OK_BUTTON).click()
        assert driver.get_title() == FolderPage.TITLE_INSIDE_DOT
        driver.get_wait(FolderPageLocator.SAVE_BUTTON)
        driver.get_element(FolderPageLocator.SAVE_BUTTON).click()
        assert driver.get_title() == FolderPage.TITLE_INSIDE_DOT_JOB
        driver.get_element(FolderPageLocator.LINK_DELETE_FOLDER).click()
        driver.get_element(FolderPageLocator.BUTTON_YES).click()

    def test_name_folder_only_one_or_two_dot(self):
        driver = FolderPage(self.driver)
        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name_only_one_or_two_dot)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        assert driver.is_element_present(FolderPageLocator.OK_BUTTON_DISABLED)
        assert driver.is_element_present(FolderPageLocator.ITEM_NAME_NOT_ALLOWED)

    def test_name_whitespace(self):
        driver = FolderPage(self.driver)
        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name_whitespace)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        driver.get_element(FolderPageLocator.OK_BUTTON).click()
        assert driver.is_element_present(FolderPageLocator.ERROR_PAGE_NONAME)

    def test_name_only_three_or_more_dots(self):
        driver = FolderPage(self.driver)
        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name_only_three_or_more_dots)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        driver.get_element(FolderPageLocator.OK_BUTTON).click()
        assert driver.is_element_present(FolderPageLocator.WRONG_REQUEST)
