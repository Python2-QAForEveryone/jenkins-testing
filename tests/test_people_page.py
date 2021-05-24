import pytest
from config.TestData import TestData
from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPage
from tests.locators_people_page import PeoplePageLocator, URLLocators
from pages.PeoplePage import PeoplePage


class TestPagePeople:
    def test_title(self):
        driver = PeoplePage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE)
        print(driver.get_title())
        assert driver.get_title() == PeoplePage.TITLE

    # def test_title(self):
    #     assert BasePage.get_title(TestData.BASE_URL + 'asynchPeople') == PeoplePage.TITLE

    @pytest.mark.parametrize('locator', PeoplePageLocator.locators_people_page)
    def test_verify_page_icon(self, locator):
        driver = PeoplePage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE)
        assert driver.is_visible(locator)

    @pytest.mark.parametrize('locator', PeoplePageLocator.locators_people_page)
    def test_verify_page_icon(self, locator):
        driver = PeoplePage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE)
        assert driver.is_clickable(locator)
