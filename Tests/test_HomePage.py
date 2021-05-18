from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class TestHomePage:

    def test_title(self):
        assert BasePage.get_title(self) == HomePage.TITLE

    def test_new_item(self):
        new_item = HomePage(self.driver)
        new_item.click(HomePage.NEW_ITEM)
        new_item.go_to_page('http://localhost:8080/')
