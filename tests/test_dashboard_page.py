import pytest

from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPage
from tests.locators_dashboard_page import DashboardPageLocators, FooterLocators, BuildLocators, AddDescriptionLocators, \
    Titles, URLLocators


class TestDashboardPage:

    def test_title(self):
        assert BasePage.get_title(self) == DashboardPage.TITLE

    def test_new_item(self):
        new_item = DashboardPage(self.driver)
        new_item.click(DashboardPage.NEW_ITEM)

    def test_dashboard_menu_anchor_is_clickable_tc_001(self):
        driver = DashboardPage(self.driver)
        assert driver.is_clickable(DashboardPageLocators.DASHBOARD_MENU_ANCHOR)

    @pytest.mark.parametrize('locator', FooterLocators.locators_for_footer)
    def test_footer_all_elements_visible_and_clickable_tc_002(self, locator):
        driver = DashboardPage(self.driver)
        assert driver.is_visible(locator)
        assert driver.is_clickable(locator)

    def test_dashboard_footer_rest_api_clickable_tc_003(self):
        driver = DashboardPage(self.driver)
        driver.click(FooterLocators.FOOTER_REST_API)
        assert driver.get_current_url() == URLLocators.URL_FOOTER_REST_API

    @pytest.mark.first
    def test_menu_selector_is_visible_and_clickable_tc_005(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.RIGHT_ARROW)
        assert driver.is_visible(DashboardPageLocators.RIGHT_ARROW_MENU_ICON)
        assert driver.is_clickable(DashboardPageLocators.RIGHT_ARROW_MENU)

    def test_right_button_all_is_clickable_tc_006(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.RIGHT_ARROW)
        driver.click(DashboardPageLocators.RIGHT_ARROW_MENU)
        assert driver.get_current_url() == URLLocators.URL_RIGHT_ARROW

    @pytest.mark.parametrize('locator', DashboardPageLocators.locators_dashboard_all,
                             ids=DashboardPageLocators.ids_dashboard_all)
    def test_dashboard_all_element_is_visible_tc_008(self, locator):
        driver = DashboardPage(self.driver)
        assert driver.is_visible(locator)

    @pytest.mark.parametrize('locator', DashboardPageLocators.locators_dashboard_text_field,
                             ids=DashboardPageLocators.ids_dashboard_text_field)
    def test_dashboard_all_element_is_clickable_tc_009(self, locator):
        driver = DashboardPage(self.driver)
        assert driver.is_clickable(locator)

    def test_dashboard_new_item_clickable_tc_010(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        assert driver.get_current_url() == URLLocators.URL_NEW_ITEM

    @pytest.mark.first
    def test_dashboard_people_clickable_tc_011(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_PEOPLE)
        assert driver.get_current_url() == URLLocators.URL_PEOPLE

    def test_dashboard_buile_history_clickable_tc_012(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_BUILD_HISTORY)
        assert driver.get_current_url() == URLLocators.URL_BUILD_HISTORY

    @pytest.mark.skip
    def test_dashboard_manage_jenkins_clickable_tc_013(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_MANAGE_JENKINS)
        assert driver.get_current_url() == URLLocators.URL_MANAGE_JENKINS

    def test_dashboard_my_view_clickable_tc_014(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_MY_VIEWS)
        assert driver.get_current_url() == URLLocators.URL_MY_VIEW

    def test_dashboard_lockable_resources_clickable_tc_015(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_LOCKABLE_RESOURCES)
        assert driver.get_current_url() == URLLocators.URL_LOCKABLE_RESOURCES

    def test_dashboard_new_view_clickable_tc_016(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_NEW_VIEW)
        assert driver.get_current_url() == URLLocators.URL_NEW_VIEW

    def test_dashboard_build_queue_executor_is_visible_tc_021(self):
        driver = DashboardPage(self.driver)
        assert driver.is_visible(BuildLocators.BUILD_QUEUE)
        assert driver.is_visible(BuildLocators.BUILD_EXECUTOR_STATUS)
        assert driver.is_clickable(BuildLocators.BUILD_EXECUTOR_STATUS)

    def test_dashboard_build_queue_executor_clickable_tc_022(self):
        driver = DashboardPage(self.driver)
        driver.click(BuildLocators.BUILD_EXECUTOR_STATUS)
        assert driver.get_current_url() == URLLocators.URL_BUILD_EXECUTOR_STATUS

    def test_dashboard_page_description_link_is_visible_tc_024(self):
        driver = DashboardPage(self.driver)
        assert driver.is_visible(AddDescriptionLocators.ADD_DESCRIPTION_LINK)
        assert driver.is_clickable(AddDescriptionLocators.ADD_DESCRIPTION_LINK)
        assert driver.is_visible(AddDescriptionLocators.ADD_DESCRIPTION_ICON)
