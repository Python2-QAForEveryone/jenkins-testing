import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Config.TestData import TestData as TD

from Pages.BasePage import BasePage
from Pages.DachboardPage import DashboardPage
from Tests import locatorsDashboardPage

class TestDashboardPage:

    @pytest.fixture(scope="class", autouse=True)
    def before_tests(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(TD.URL)
        search_field_login = driver.find_element(By.CSS_SELECTOR, '#j_username')
        search_field_login.send_keys(TD.LOGIN)
        search_field_password = driver.find_element(By.CSS_SELECTOR, 'input[name="j_password"]')
        search_field_password.send_keys(TD.PASSWORD)
        search_button = driver.find_element(By.CSS_SELECTOR, 'input[name="Submit"]').click()

        yield
        driver.quit()


    def test_tc_001_dashboard_menu_anchor(self):
        driver = DashboardPage(self.driver)
        assert BasePage.is_clickable(locatorsDashboardPage.DASHBOARD_MENU_ANCHOR)


    def test_tc_002_footer_all_elements_visible_and_clickable(self):
        driver = DashboardPage(self.driver)
        assert BasePage.is_visible(locatorsDashboardPage.FOOTER_REST_API)
        assert BasePage.is_visible(locatorsDashboardPage.FOOTER_VERSION)
        assert BasePage.is_clickable(locatorsDashboardPage.FOOTER_REST_API)
        assert BasePage.is_clickable(locatorsDashboardPage.FOOTER_VERSION)

    def test_tc_008_dashboard_all_element_is_visible(self):
        driver = DashboardPage(self.driver)
        assert BasePage.is_visible(locatorsDashboardPage.TEXT_NEW_ITEM)
        assert BasePage.is_visible(locatorsDashboardPage.ICON_NEW_ITEM)
        assert BasePage.is_visible(locatorsDashboardPage.TEXT_PEOPLE)
        assert BasePage.is_visible(locatorsDashboardPage.ICON_PEOPLE)
        assert BasePage.is_visible(locatorsDashboardPage.TEXT_BUILD_HISTORY)
        assert BasePage.is_visible(locatorsDashboardPage.ICON_BUILD_HISTORY)
        assert BasePage.is_visible(locatorsDashboardPage.TEXT_MANAGE_JENKINS)
        assert BasePage.is_visible(locatorsDashboardPage.ICON_MANAGE_JENKINS)
        assert BasePage.is_visible(locatorsDashboardPage.TEXT_MY_VIEWS)
        assert BasePage.is_visible(locatorsDashboardPage.ICON_MY_VIEWS)
        assert BasePage.is_visible(locatorsDashboardPage.TEXT_LOCKABLE_RESOURCES)
        assert BasePage.is_visible(locatorsDashboardPage.ICON_LOCKABLE_RESOURCES)
        assert BasePage.is_visible(locatorsDashboardPage.TEXT_NEW_VIEW)
        assert BasePage.is_visible(locatorsDashboardPage.ICON_NEW_VIEW)


    def test_tc_009_dashboard_all_element_is_clickable(self):
        driver = DashboardPage(self.driver)
        assert BasePage.is_clickable(locatorsDashboardPage.TEXT_NEW_ITEM)
        assert BasePage.is_clickable(locatorsDashboardPage.TEXT_PEOPLE)
        assert BasePage.is_clickable(locatorsDashboardPage.TEXT_BUILD_HISTORY)
        assert BasePage.is_clickable(locatorsDashboardPage.TEXT_MANAGE_JENKINS)
        assert BasePage.is_clickable(locatorsDashboardPage.TEXT_MY_VIEWS)
        assert BasePage.is_clickable(locatorsDashboardPage.TEXT_LOCKABLE_RESOURCES)
        assert BasePage.is_clickable(locatorsDashboardPage.TEXT_NEW_VIEW)


    def test_tc_021_dashboard_build_queue_executor_is_visible(self):
        driver = DashboardPage(self.driver)
        assert BasePage.is_visible(locatorsDashboardPage.BUILD_QUEUE)
        assert BasePage.is_visible(locatorsDashboardPage.BUILD_EXECUTOR_STATUS)
        assert BasePage.is_clickable(locatorsDashboardPage.BUILD_EXECUTOR_STATUS)