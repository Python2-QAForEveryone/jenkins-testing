from pages.DashboardLowerDropdownPage import DashboardLowerDropdownPage
from tests.locatorsDashboardLowerDropdown import DashboardLowerDropdownPageLocators

class TestDashboardLowerDropdownPage:

    def test_dashboard_link_is_visible_and_clickable(self):
        driver = DashboardLowerDropdownPage(self.driver)
        assert driver.is_clickable(DashboardLowerDropdownPageLocators.DASHBOARD_LINK)
        assert driver.is_visible(DashboardLowerDropdownPageLocators.DASHBOARD_LINK)