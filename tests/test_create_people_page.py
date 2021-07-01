import random
import string
import time
from pages.CreateUserPage import CreateUserPage

from selenium.webdriver.common.by import By

from pages.CreateUserPage import CreateUserPage
from tests.locators_people_page import URLLocators


class TestCreatePeoplePage:
    name = (''.join(random.choice(string.ascii_letters) for i in range(10)))

    def test_create_people(self):
        driver = CreateUserPage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE_CREATE)

        # self.driver.enter_username(self.name)
        driver.do_send_keys(CreateUserPage.user, "user2")
        driver.enter_password("123")
        driver.enter_confirm_password("123")
        driver.enter_fullname(f"User {self.name}")
        driver.enter_email(f"{self.name}@gmail.com")
        self.driver.click_create_button()

        self.driver.go_to_page(URLLocators.URL_PEOPLE)
        field = self.driver.get_element_text((By.XPATH, f'//tr[@id=\'person-{self.name}\']')).split(' ')

        assert field[0] == self.name

    def test_delete_user(self):
        # driver = CreateUserPage(self.driver)
        self.driver.go_to_page(URLLocators.URL_PEOPLE)
        time.sleep(3)
        user_delete = self.driver.find_element_by_xpath(f"//a[contains(text(),'{self.name}')]")
        print(user_delete)
        # user_delete.click()
        #
        # button_delete = driver.find_element_by_xpath(f"//a[contains(@href, '/user/{self.name.lower()}/delete')]")
        # button_delete.click()
        # driver.find_element_by_id("yui-gen1-button").click()
