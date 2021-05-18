from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Tests.locators_HomePage import DashboardPageLocators


class TestHomePage:

    def test_title(self):
        assert BasePage.get_title(self) == HomePage.TITLE

    def test_new_item(self):
        new_item = HomePage(self.driver)
        new_item.click(HomePage.NEW_ITEM)
        new_item.go_to_page('http://localhost:8080/')

    def test_dashboard_menu_anchor_is_clickable_tc_001(self):
        assert BasePage.is_clickable(DashboardPageLocators.DASHBOARD_MENU_ANCHOR)
