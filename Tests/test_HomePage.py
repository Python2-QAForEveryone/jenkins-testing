import pytest

from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Tests.locators_HomePage import DashboardPageLocators, FooterLocators, BuildLocators, AddDescriptionLocators


class TestHomePage:

    def test_title(self):
        assert BasePage.get_title(self) == HomePage.TITLE

    def test_new_item(self):
        new_item = HomePage(self.driver)
        new_item.click(HomePage.NEW_ITEM)
        new_item.go_to_page('http://localhost:8080/')

    def test_dashboard_menu_anchor_is_clickable_tc_001(self):
        home_page = HomePage(self.driver)
        assert home_page.is_clickable(DashboardPageLocators.DASHBOARD_MENU_ANCHOR)

    @pytest.mark.parametrize('locator', FooterLocators.locators_for_footer)
    def test_footer_all_elements_visible_and_clickable_tc_002(self, locator):
        home_page = HomePage(self.driver)
        assert home_page.is_visible(locator)
        assert home_page.is_clickable(locator)

    @pytest.mark.parametrize('locator', DashboardPageLocators.locators_dashboard_all)
    def test_dashboard_all_element_is_visible_tc_008(self, locator):
        assert BasePage.is_visible(locator)

    @pytest.mark.parametrize('locator', DashboardPageLocators.locators_dashboard_text_field)
    def test_dashboard_all_element_is_clickable_tc_009(self, locator):
        assert BasePage.is_clickable(locator)

    def test_dashboard_build_queue_executor_is_visible_tc_021(self):
        assert BasePage.is_visible(BuildLocators.BUILD_QUEUE)
        assert BasePage.is_visible(BuildLocators.BUILD_EXECUTOR_STATUS)
        assert BasePage.is_clickable(BuildLocators.BUILD_EXECUTOR_STATUS)

    def test_dashboard_page_description_link_is_visible_tc_024(self):
        assert BasePage.is_visible(AddDescriptionLocators.ADD_DESCRIPTION_LINK)
        assert BasePage.is_clickable(AddDescriptionLocators.ADD_DESCRIPTION_LINK)
        assert BasePage.is_visible(AddDescriptionLocators.ADD_DESCRIPTION_ICON)