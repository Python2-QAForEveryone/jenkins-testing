from selenium.webdriver.common.by import By

from config.TestData import TestData


class DashboardLowerDropdownPageLocators:
    DASHBOARD_LINK = (By.XPATH, "//a[text()='Dashboard']")
    MENU_SELECTOR = (By.ID, 'menuSelector')

class DashboardLowerDropdownLocators:
    NEW_ITEM = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'newJob')]"))
    PEOPLE = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'People')]"))
    BUILD_HISTORY = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'builds')]"))
    MANAGE_JENKINS = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'manage')]"))
    MY_VIEWS = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'my-views')]"))
    LOCKABLE_RESOURCES = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'lockable-resources')]"))
    NEW_VIEW = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'newView')]"))

    locators_for_dropdown = [NEW_ITEM, PEOPLE, BUILD_HISTORY, MANAGE_JENKINS, MY_VIEWS, LOCKABLE_RESOURCES, NEW_VIEW]

    ids_dropdown = ['NEW_ITEM', 'PEOPLE', 'BUILD_HISTORY', 'MANAGE_JENKINS',
                    'MY_VIEWS', 'LOCKABLE_RESOURCES', 'NEW_VIEW']
