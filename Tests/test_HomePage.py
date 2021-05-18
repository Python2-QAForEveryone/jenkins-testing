from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
import time

class TestHomePage:

    def test_title(self):
        assert BasePage.get_title(self) == HomePage.TITLE

    def test_new_item(self):
        new_item = HomePage(self.driver)
        time.sleep(3)
        new_item.click(HomePage.NEW_ITEM)
        time.sleep(3)
        new_item.go_to_page('http://localhost:8080/')
        time.sleep(3)

