from pages.BasePage import BasePage
from pages.BuildHistoryPage import BuildHistoryPage
import pytest
import time


class TestBuildHistory:

    def test_buildhistoryurlvisible(self):
        bhp_driver = BuildHistoryPage(self.driver)
        bhp_driver.go_to_page(BuildHistoryPage.page_url)
        curr_url = str(bhp_driver.get_currenturl())
        assert (BuildHistoryPage.href in curr_url)

    # @pytest.mark.skip
    # def test_build_history_logo_visible(self):
    #     bhp_driver = BuildHistoryPage(self.driver)
    #     bhp_driver.go_to_page(BuildHistoryPage.page_url)
    #     assert bhp_driver.is_visible(BuildHistoryPage.bhpage_image)
    #
    # def test_build_history_table_header_visible(self):
    #     bhp_driver = BuildHistoryPage(self.driver)
    #     bhp_driver.go_to_page(BuildHistoryPage.page_url)
    #     assert bhp_driver.is_visible(BuildHistoryPage.table_header)
    #
    # def test_build_history_header_build_btn_clickable(self):
    #     bhp_driver = BuildHistoryPage(self.driver)
    #     bhp_driver.go_to_page(BuildHistoryPage.page_url)
    #     assert bhp_driver.is_clickable(BuildHistoryPage.project_status_buttn)
