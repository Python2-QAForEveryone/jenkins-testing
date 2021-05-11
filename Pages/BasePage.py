from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        super(BasePage, self).__init__()
        self.page_url = str()
        self.driver = driver

    def is_visible(self):
        condition = EC.visibility_of_element_located(self)
        return bool(condition)

    def is_hidden(self):
        condition = EC.visibility_of_element_located(self)
        return bool(not condition)

    def is_clickable(self):
        condition = EC.element_to_be_clickable(self)
        return bool(condition)

    def click(self, locator):
        element = self.driver.find_element(locator[0], locator[1])
        element.click()

    def go_to_page(self):
        self.driver.get(self.page_url)
        return self

    def get_title(self):
        return self.driver.title

    def send_key(self, locator, value):
        element = self.driver.find_element(locator[0], locator[1])
        element.send_keys(value)

    def get_url(self):
        get_url = self.driver.current_url
        return get_url
