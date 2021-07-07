import random
import string

from pages.CreateUserPage import CreateUserPage
from pages.PeoplePage import URLLocators


class TestCreateUserPage:
    name = (''.join(random.choice(string.ascii_letters) for i in range(10)))

    def test_create_user(self):
        driver = CreateUserPage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE_CREATE)

        driver.do_send_keys(CreateUserPage.username_id, CreateUserPage.name)
        driver.do_send_keys(CreateUserPage.password_input_name, "123")
        driver.do_send_keys(CreateUserPage.enter_confirm_password, "123")
        driver.do_send_keys(CreateUserPage.fullname_name, f"User {CreateUserPage.name}")
        driver.do_send_keys(CreateUserPage.email_name, f"{CreateUserPage.name}@gmail.com")
        driver.click(CreateUserPage.button_create_id)

        driver.go_to_page(URLLocators.URL_PEOPLE)
        field = driver.get_element_text(CreateUserPage.USER_NAME).split(' ')

        assert field[0] == CreateUserPage.name

    def test_delete_user(self):
        driver = CreateUserPage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE)

        driver.get_element(CreateUserPage.PEOPLE_DELETE).click()
        driver.get_element(CreateUserPage.BUTTON_DELETE).click()
        driver.get_element(CreateUserPage.BUTTON_YES).click()

        driver.go_to_page(URLLocators.URL_PEOPLE)

        assert driver.is_element_not_present(CreateUserPage.PEOPLE_DELETE)
