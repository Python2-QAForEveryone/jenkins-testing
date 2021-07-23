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
        driver.get_element(FolderPageLocator.LINK_FOLDER).click()
        driver.get_element(FolderPageLocator.OK_BUTTON).click()

        assert driver.get_title() == FolderPage.WRONG_TITLE
        assert driver.is_element_present(FolderPageLocator.WRONG_REQUEST)

