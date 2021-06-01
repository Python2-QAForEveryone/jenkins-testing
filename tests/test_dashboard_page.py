import pytest

from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPage
from config.TestData import TestData as TD
from tests.locators_dashboard_page import DashboardPageLocators, FooterLocators, BuildLocators, AddDescriptionLocators, \
    Titles, URLLocators


class TestDashboardPage:

    def test_title(self):
        assert BasePage.get_title(self) == DashboardPage.TITLE

    def test_new_item(self):
        new_item = DashboardPage(self.driver)
        new_item.click(DashboardPage.NEW_ITEM)
        new_item.go_to_page(TD.BASE_URL)

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
        driver.go_to_page(TD.BASE_URL)

    def test_menu_selector_can_be_click_tc_005(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.RIGHT_ARROW_SELECTOR)
        assert driver.is_visible(DashboardPageLocators.RIGHT_ARROW_SELECTOR_ALL_VISIBLE)
        driver.click(DashboardPageLocators.RIGHT_ARROW_SELECTOR_ALL)
        assert driver.get_title() == Titles.TITLE_DASHBOARD_PAGE
        driver.go_to_page(TD.BASE_URL)

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
        driver.go_to_page(TD.BASE_URL)

    def test_dashboard_people_clickable_tc_011(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_PEOPLE)
        assert driver.get_current_url() == URLLocators.URL_PEOPLE
        driver.go_to_page(TD.BASE_URL)

    def test_dashboard_buile_history_clickable_tc_012(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_BUILD_HISTORY)
        assert driver.get_current_url() == URLLocators.URL_BUILD_HISTORY
        driver.go_to_page(TD.BASE_URL)


    def test_dashboard_manage_jenkins_clickable_tc_013(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_MANAGE_JENKINS)
        assert driver.get_current_url() == URLLocators.URL_MANAGE_JENKINS
        driver.go_to_page(TD.BASE_URL)

    def test_dashboard_my_view_clickable_tc_014(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_MY_VIEWS)
        assert driver.get_current_url() == URLLocators.URL_MY_VIEW
        driver.go_to_page(TD.BASE_URL)

    def test_dashboard_lockable_resources_clickable_tc_015(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_LOCKABLE_RESOURCES)
        assert driver.get_current_url() == URLLocators.URL_LOCKABLE_RESOURCES
        driver.go_to_page(TD.BASE_URL)

    def test_dashboard_new_view_clickable_tc_016(self):
        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_NEW_VIEW)
        assert driver.get_current_url() == URLLocators.URL_NEW_VIEW
        driver.go_to_page(TD.BASE_URL)

    def test_dashboard_build_queue_executor_is_visible_tc_021(self):
        driver = DashboardPage(self.driver)
        assert driver.is_visible(BuildLocators.BUILD_QUEUE)
        assert driver.is_visible(BuildLocators.BUILD_EXECUTOR_STATUS)
        assert driver.is_clickable(BuildLocators.BUILD_EXECUTOR_STATUS)

    def test_dashboard_build_queue_executor_clickable_tc_022(self):
        driver = DashboardPage(self.driver)
        driver.click(BuildLocators.BUILD_EXECUTOR_STATUS)
        assert driver.get_current_url() == URLLocators.URL_BUILD_EXECUTOR_STATUS
        driver.go_to_page(TD.BASE_URL)

    def test_dashboard_page_description_link_is_visible_tc_024(self):
        driver = DashboardPage(self.driver)
        assert driver.is_visible(AddDescriptionLocators.ADD_DESCRIPTION_LINK)
        assert driver.is_clickable(AddDescriptionLocators.ADD_DESCRIPTION_LINK)
        assert driver.is_visible(AddDescriptionLocators.ADD_DESCRIPTION_ICON)
