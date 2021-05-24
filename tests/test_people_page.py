import time

import pytest

from pages.BasePage import BasePage
from pages.PeoplePage import PeoplePage
from tests.locators_people_page import PeoplePageLocator, URLLocators, IdUsersLocator


class TestPagePeople:
    def test_people_title_001(self):
        driver = PeoplePage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE)
        assert driver.get_title() == PeoplePage.TITLE

    @pytest.mark.parametrize('locator', PeoplePageLocator.locators_people_page)
    def test_all_element_is_visible_002(self, locator):
        driver = PeoplePage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE)
        assert driver.is_visible(locator)

    @pytest.mark.parametrize('locator', PeoplePageLocator.locators_people_page)
    def test_all_element_is_clickable_003(self, locator):
        driver = PeoplePage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE)
        assert driver.is_clickable(locator)