from selenium.webdriver.common.by import By

from config.TestData import TestData
from pages.BasePage import BasePage


class PeoplePage(BasePage):
    """
    initialized driver
    added moving to the BasePage after log in
    """

    def __init__(self, driver):
        super().__init__(driver)

    TITLE = "People - [Jenkins]"


class PeoplePageLocator:
    PEOPLE = (By.CSS_SELECTOR, '.task-link--active')
    PEOPLE_LOGO = (By.CSS_SELECTOR, '.icon-xlg')
    TABLE_USER_ID = (By.XPATH, '//a[contains(text(),"User ID")]')
    TABLE_USER_ID_ARROW = (By.XPATH, '//th[2]/a/span')
    TABLE_NAME = (By.XPATH, '//a[contains(text(),"Name")]')
    TABLE_NAME_ARROW = (By.XPATH, '//th[3]/a/span')
    TABLE_LAST_COMMIT_ACTIVITY = (By.XPATH, '//a[contains(text(),"Last Commit Activity")]')
    TABLE_LAST_COMMIT_ACTIVITY_ARROW = (By.XPATH, '//th[4]/a/span')
    TABLE_ON = (By.XPATH, '//a[contains(text(),"On")]')
    TABLE_ON_ARROW = (By.XPATH, '//th[5]/a/span')
    TABLE_ICON = (By.XPATH, '//*[@id="person-users"]/td[1]/a/img')
    TABLE_USER_ID_USERS = (By.XPATH, '//td[3]/a')
    TABLE_NAME_USERS = (By.XPATH, '//td[3]/a')
    TABLE_ICON_LINK_S = (By.LINK_TEXT, 'S')
    TABLE_ICON_LINK_M = (By.LINK_TEXT, 'M')
    TABLE_ICON_LINK_L = (By.LINK_TEXT, 'L')

    locators_people_page = [PEOPLE, PEOPLE_LOGO, TABLE_USER_ID, TABLE_USER_ID_ARROW, TABLE_NAME, TABLE_NAME_ARROW,
                            TABLE_LAST_COMMIT_ACTIVITY, TABLE_LAST_COMMIT_ACTIVITY_ARROW, TABLE_ON, TABLE_ON_ARROW,
                            TABLE_USER_ID_USERS, TABLE_NAME_USERS, TABLE_ICON_LINK_S, TABLE_ICON_LINK_M]


class URLLocators:
    URL_PEOPLE = TestData.BASE_URL + 'asynchPeople/'
    URL_PEOPLE_CREATE = TestData.BASE_URL + 'securityRealm/addUser'


class IdUsersLocator:
    TABLE_USER_ID_ARROW = (By.XPATH, '//*[@id="people"]/tbody/tr[1]/th[2]/a/span')
    locator_id_user_arrow = [TABLE_USER_ID_ARROW]
    TABLE_USER_ID = (By.XPATH, '//*[@id="people"]/tbody/tr[1]/th[2]/a')
    locator_id_user = [TABLE_USER_ID]
