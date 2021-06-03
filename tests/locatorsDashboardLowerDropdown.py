from selenium.webdriver.common.by import By

from config.TestData import TestData

class DashboardLowerDropdownPageLocators:

    DASHBOARD_LINK = (By.XPATH, "//a[text()='Dashboard']")
    MENU_SELECTOR = (By.ID, 'menuSelector')
    RIGHT_ARROW_SELECTOR = (By.CLASS_NAME, 'children')
    RIGHT_ARROW_SELECTOR_ALL = (By.XPATH, '//a[@href="/view/all/"]')
    RIGHT_ARROW_SELECTOR_ALL_VISIBLE = (By.ID, 'breadcrumb-menu')

