from pages.BasePage import BasePage


class CreateUserPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    username_id = "username"
    password_input_name = "password1"
    password_confirm_name = "password2"
    fullname_name = "fullname"
    email_name = "email"
    button_create_id = "yui-gen1-button"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_input_name).clear()
        self.driver.find_element_by_name(self.password_input_name).send_keys(password)

    def enter_confirm_password(self, password):
        self.driver.find_element_by_name(self.password_confirm_name).clear()
        self.driver.find_element_by_name(self.password_confirm_name).send_keys(password)

    def enter_fullname(self, fullname):
        self.driver.find_element_by_name(self.fullname_name).clear()
        self.driver.find_element_by_name(self.fullname_name).send_keys(fullname)

    def enter_email(self, email):
        self.driver.find_element_by_name(self.email_name).clear()
        self.driver.find_element_by_name(self.email_name).send_keys(email)

    def click_create_button(self):
        self.driver.find_element_by_id(self.button_create_id).click()

    def find_element_by_xpath(self, locator):
        self.driver.find_element_by_xpath(locator)

    def find_element_by_link_text(self, text):
        self.driver.find_element_by_link_text(text)

    def find_element_by_id(self, _id):
        self.find_element_by_id(_id)
