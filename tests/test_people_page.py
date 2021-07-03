import pytest

from pages.PeoplePage import PeoplePage
from pages.PeoplePage import PeoplePageLocator, URLLocators


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
