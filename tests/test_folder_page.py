from pages.FolderPage import FolderPage
from pages.FolderPage import FolderPageLocator, URLLocators


class TestFolderPage:

    def test_create_folder(self):
        driver = FolderPage(self.driver)
        driver.go_to_page(URLLocators.URL_FOLDER_CREATE)

        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        driver.get_element(FolderPageLocator.OK_BUTTON).click()

        assert driver.get_title() == FolderPage.TITLE

    def test_name_folder_more_255_ch(self):
        driver = FolderPage(self.driver)
        driver.go_to_page(URLLocators.URL_FOLDER_CREATE)

        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.long_name)
        print(FolderPage.long_name)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        driver.get_element(FolderPageLocator.OK_BUTTON).click()

        assert driver.get_title() == FolderPage.WRONG_TITLE
        assert driver.is_element_present(FolderPageLocator.WRONG_REQUEST)

    def test_name_folder_start_special_ch(self):
        driver = FolderPage(self.driver)
        driver.go_to_page(URLLocators.URL_FOLDER_CREATE)

        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name_start_special_ch)
        print(FolderPage.name_start_special_ch)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()

        assert driver.is_element_present(FolderPageLocator.ITEM_NAME_INVALID)

    def test_name_folder_inside_special_ch(self):
        driver = FolderPage(self.driver)
        driver.go_to_page(URLLocators.URL_FOLDER_CREATE)

        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name_inside_special_ch)
        print(FolderPage.name_inside_special_ch)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()

        assert driver.is_element_present(FolderPageLocator.ITEM_NAME_INVALID)

        driver.get_element(FolderPageLocator.OK_BUTTON).click()

        assert driver.is_element_present(FolderPageLocator.ERROR_PAGE)

    def test_name_folder_digits(self):
        driver = FolderPage(self.driver)
        driver.go_to_page(URLLocators.URL_FOLDER_CREATE)

        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name_digits)
        print(FolderPage.name_digits)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        driver.get_element(FolderPageLocator.OK_BUTTON).click()

        assert driver.get_title() == FolderPage.TITLE_DIGITS

    def test_name_folder_empty(self):
        driver = FolderPage(self.driver)
        driver.go_to_page(URLLocators.URL_FOLDER_CREATE)

        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name_empty)
        print("!" + FolderPage.name_empty + "!")
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()

        assert driver.is_element_present(FolderPageLocator.ITEM_NAME_REQUIRED)

    def test_name_folder_start_dot(self):
        driver = FolderPage(self.driver)
        driver.go_to_page(URLLocators.URL_FOLDER_CREATE)

        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name_start_dot)
        print(FolderPage.name_start_dot)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()

        assert driver.is_element_present(FolderPageLocator.ITEM_NAME_NOT_ALLOWED)

    def test_name_folder_inside_dot(self):
        driver = FolderPage(self.driver)
        driver.go_to_page(URLLocators.URL_FOLDER_CREATE)

        driver.do_send_keys(FolderPageLocator.ITEM_NAME, FolderPage.name_inside_dot)
        print(FolderPage.name_inside_dot)
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        driver.get_element(FolderPageLocator.OK_BUTTON).click()

        assert driver.get_title() == FolderPage.TITLE_DOT
