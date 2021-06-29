import random
import string
import time

from selenium.webdriver.common.by import By

from pages.CreateUserPage import CreateUserPage
from tests.locators_people_page import URLLocators


class TestCreatePeoplePage:

    def test_create_people(self):
        name = (''.join(random.choice(string.ascii_letters) for i in range(10)))

        driver = CreateUserPage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE_CREATE)

        driver.enter_username(name)
        driver.enter_password("123")
        driver.enter_confirm_password("123")
        driver.enter_fullname(f"User {name}")
        driver.enter_email(f"{name}@gmail.com")
        driver.click_create_button()

        driver.go_to_page(URLLocators.URL_PEOPLE)
        field = driver.get_element_text((By.XPATH, f'//tr[@id=\'person-{name}\']')).split(' ')

        assert field[0] == name

        driver.go_to_page(URLLocators.URL_PEOPLE)

        user_delete = self.driver.find_element_by_xpath(f"//a[contains(text(),'{name}')]")
        user_delete.click()

        button_delete = self.driver.find_element_by_xpath(f"//a[contains(@href, '/user/{name.lower()}/delete')]")
        button_delete.click()
        self.driver.find_element_by_id("yui-gen1-button").click()
