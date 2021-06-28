import pytest
from pages.GlobalToolConfiguration import GlobalToolConfiguration
from tests.locators_globaltoolconfigpage import NavigatetoGlobToolConfigLocators, HeadersLocators, ButtonLocators, \
    Urllocators


class TestGlobalPage:
    def test_global_title(self):
        driver = GlobalToolConfiguration(self.driver)
        driver.hover_over_element(NavigatetoGlobToolConfigLocators.DASHBOARD_LINK)
        driver.click(NavigatetoGlobToolConfigLocators.PULLDOWN_ARROW)
        driver.get_wait(NavigatetoGlobToolConfigLocators.MANAGE_JENKINS_SUBMENU)
        driver.hover_over_element(NavigatetoGlobToolConfigLocators.MANAGE_JENKINS_SUBMENU)
        driver.get_wait(NavigatetoGlobToolConfigLocators.GLOBTOOLGONG_SUBMENU)
        driver.hover_element1_and_click_element2(NavigatetoGlobToolConfigLocators.GLOBTOOLGONG_SUBMENU,
                                                 NavigatetoGlobToolConfigLocators.GLOBTOOLGONG_SUBMENU)
        driver.get_wait(NavigatetoGlobToolConfigLocators.PAGE_TITLE)
        assert driver.get_title() == GlobalToolConfiguration.TITLE

    @pytest.mark.parametrize("locator", HeadersLocators.locators_globtoolpage_all,
                             ids = HeadersLocators.ids_globtoolpage_all)
    def test_glob_locators_visible(self, locator):
        driver = GlobalToolConfiguration(self.driver)
        driver.go_to_page(Urllocators.URL_GLOBAL)
        assert driver.is_visible(locator)

    @pytest.mark.parametrize("locators", ButtonLocators.locators_buttons,
                             ids = ButtonLocators.ids_buttons)
    def test_glob_button_locators_clickable(self, locators):
        driver = GlobalToolConfiguration(self.driver)
        driver.go_to_page(Urllocators.URL_GLOBAL)
        assert driver.is_clickable(locators)