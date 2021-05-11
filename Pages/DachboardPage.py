from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.TestData import TestData as TD
import Tests.locatorsDashboardPage


class DashboardPage(BasePage):


    def __init__(self, driver):
        super(DashboardPage, self).__init__(driver)
        self.page_url = TD.URL
        self.driver = driver
