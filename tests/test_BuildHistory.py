from pages.BasePage import BasePage
from pages.BuildHistoryPage import BuildHistoryPage
import pytest
import time
class TestBuildHistory:

    def test_buildhistoryurlvisible(self):
        bhp = BuildHistoryPage(self.driver)
        bhp.go_to_page(BuildHistoryPage.page_url)
        curr_url = str(bhp.get_currenturl())
        assert (BuildHistoryPage.href in curr_url)

    def test_build_history_logovisible(self):
        bhp = BuildHistoryPage(self.driver)
        bhp.go_to_page(BuildHistoryPage.page_url)
        assert bhp.is_visible(BuildHistoryPage.pict)

    def test_build_history_header_buildbtnclickable(self):
        bhp = BuildHistoryPage(self.driver)
        bhp.go_to_page(BuildHistoryPage.page_url)
        assert bhp.is_clickable(BuildHistoryPage.header_btn1)
