from selenium.webdriver.common.by import By

from config.TestData import TestData

class DashboardLowerDropdownPageLocators:

    DASHBOARD_LINK = (By.XPATH, "//a[text()='Dashboard']")
    MENU_SELECTOR = (By.ID, 'menuSelector')
    RIGHT_ARROW_SELECTOR = (By.CLASS_NAME, 'children')
    RIGHT_ARROW_SELECTOR_ALL = (By.XPATH, '//a[@href="/view/all/"]')
    RIGHT_ARROW_SELECTOR_ALL_VISIBLE = (By.ID, 'breadcrumb-menu')
    NEW_ITEM = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'newJob')]"))
    PEOPLE = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'People')]"))
    BUILD_HISTORY = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'builds')]"))
    MANAGE_JENKINS = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'manage')]"))
    MY_VIEWS = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'my-views')]"))
    LOCKABLE_RESOURCES = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'lockable-resources')]"))
    NEW_VIEW = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'newView')]"))
