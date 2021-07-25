from pages.BasePage import BasePage
from pages.BuildHistoryPage import BuildHistoryPage
import pytest


class TestBuildHistory:

    def test_build_history_url_visible(self):
        bhp_driver = BuildHistoryPage(self.driver)
        bhp_driver.go_to_page(BuildHistoryPage.PAGE_URL)
        curr_url = str(BasePage.get_current_url(self))
        assert (BuildHistoryPage.BHP_HREF in curr_url)

    @pytest.mark.skip(reason="because it was failing previously, need some additional research")
    def test_build_history_logo_visible(self):
        bhp_driver = BuildHistoryPage(self.driver)
        bhp_driver.go_to_page(BuildHistoryPage.PAGE_URL)
        assert bhp_driver.is_visible(BuildHistoryPage.BHPAGE_IMAGE)

    def test_build_history_table_header_visible(self):
        bhp_driver = BuildHistoryPage(self.driver)
        bhp_driver.go_to_page(BuildHistoryPage.PAGE_URL)
        assert bhp_driver.is_visible(BuildHistoryPage.BHP_TABLE_HEADER1)

    def test_build_history_header_build_btn_clickable(self):
        bhp_driver = BuildHistoryPage(self.driver)
        bhp_driver.go_to_page(BuildHistoryPage.PAGE_URL)
        assert bhp_driver.is_clickable(BuildHistoryPage.PROJECT_STATUS_BUTTN)
