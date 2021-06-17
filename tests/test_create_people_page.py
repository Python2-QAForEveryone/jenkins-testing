from pages.CreateUserPage import CreateUserPage
from tests.locators_people_page import URLLocators
from tests.locators_people_page import InputFormNewUser


class TestCreatePeoplePage:

    def test_create_people(self):
        driver = CreateUserPage(self.driver)
        driver.go_to_page(URLLocators.URL_PEOPLE_CREATE)

        driver.enter_username("user1")
        driver.enter_password("123")
        driver.enter_confirm_password("123")
        driver.enter_fullname("User User")
        driver.enter_email("user@gmail.com")
        driver.click_create_button()

        driver.go_to_page(URLLocators.URL_PEOPLE)
        field = driver.get_element_text(InputFormNewUser.FIELD_NEW_USER).split(' ')

        assert field[0] == "user1"
