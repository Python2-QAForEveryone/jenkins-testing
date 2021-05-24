from selenium.webdriver.common.by import By

from config.TestData import TestData

TITLE = "People - [Jenkins]"


class PeoplePageLocator:
    PEOPLE = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/div[2]/span/a/span[2]')
    PEOPLE_LOGO = (By.XPATH, '/html/body/div[4]/div[2]/h1/img')
    TABLE_USER_ID = (By.XPATH, '//*[@id="people"]/tbody/tr[1]/th[2]/a')
    TABLE_USER_ID_ARROW = (By.XPATH, '//*[@id="people"]/tbody/tr[1]/th[2]/a/span')
    TABLE_NAME = (By.XPATH, '//*[@id="people"]/tbody/tr[1]/th[3]/a')
    TABLE_NAME_ARROW = (By.XPATH, '//*[@id="people"]/tbody/tr[1]/th[3]/a/span')
    TABLE_LAST_COMMIT_ACTIVITY = (By.XPATH, '//*[@id="people"]/tbody/tr[1]/th[4]/a')
    TABLE_LAST_COMMIT_ACTIVITY_ARROW = (By.XPATH, '//*[@id="people"]/tbody/tr[1]/th[4]/a/span')
    TABLE_ON = (By.XPATH, '//*[@id="people"]/tbody/tr[1]/th[5]/a')
    TABLE_ON_ARROW = (By.XPATH, '//*[@id="people"]/tbody/tr[1]/th[5]/a/span')
    TABLE_ICON = (By.XPATH, '//*[@id="person-users"]/td[1]/a/img')
    TABLE_USER_ID_USERS = (By.XPATH, '/html/body/div[4]/div[2]/table[2]/tbody/tr[2]/td[2]/a')
    TABLE_NAME_USERS = (By.XPATH, '/html/body/div[4]/div[2]/table[2]/tbody/tr[2]/td[3]/a')
    TABLE_ICON_LINK = (By.XPATH, '/html/body/div[4]/div[2]/table[3]/tbody/tr/td[1]/a[1]')
    TABLE_ICON_LINK_2 = (By.XPATH, '/html/body/div[4]/div[2]/table[3]/tbody/tr/td[1]/a[2]')

    locators_people_page = [PEOPLE, PEOPLE_LOGO, TABLE_USER_ID, TABLE_USER_ID_ARROW, TABLE_NAME, TABLE_NAME_ARROW,
                            TABLE_LAST_COMMIT_ACTIVITY, TABLE_LAST_COMMIT_ACTIVITY_ARROW, TABLE_ON, TABLE_ON_ARROW,
                            TABLE_USER_ID_USERS, TABLE_NAME_USERS, TABLE_ICON_LINK, TABLE_ICON_LINK_2]


class URLLocators:
    URL_PEOPLE = TestData.BASE_URL + 'asynchPeople/'


class IdUsersLocator:
    TABLE_USER_ID_ARROW = (By.XPATH, '//*[@id="people"]/tbody/tr[1]/th[2]/a/span')
    locator_id_user_arrow = [TABLE_USER_ID_ARROW]
    TABLE_USER_ID = (By.XPATH, '//*[@id="people"]/tbody/tr[1]/th[2]/a')
    locator_id_user = [TABLE_USER_ID]
