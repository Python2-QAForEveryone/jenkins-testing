from pages.DashboardLowerDropdownPage import DashboardLowerDropdownPage
from tests.locatorsDashboardLowerDropdown import DashboardLowerDropdownPageLocators

class TestDashboardLowerDropdownPage:

    def test_dashboard_link_is_visible_and_clickable(self):
        driver = DashboardLowerDropdownPage(self.driver)
        assert driver.is_clickable(DashboardLowerDropdownPageLocators.DASHBOARD_LINK)
        assert driver.is_visible(DashboardLowerDropdownPageLocators.DASHBOARD_LINK)

    def test_dashboard_down_arrow_is_visible_and_clickable(self):
        driver = DashboardLowerDropdownPage(self.driver)
        driver.hover_over_element(DashboardLowerDropdownPageLocators.DASHBOARD_LINK)
        assert driver.is_visible(DashboardLowerDropdownPageLocators.MENU_SELECTOR)
        assert driver.is_clickable(DashboardLowerDropdownPageLocators.MENU_SELECTOR)

    def test_dashboard_lower_dropdown_items_clickable(self):
        driver = DashboardLowerDropdownPage(self.driver)
        driver.hover_and_click_element(DashboardLowerDropdownPageLocators.DASHBOARD_LINK,
                                            DashboardLowerDropdownPageLocators.MENU_SELECTOR)
        assert driver.is_clickable(DashboardLowerDropdownPageLocators.NEW_ITEM)