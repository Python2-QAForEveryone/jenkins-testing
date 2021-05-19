from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def go_to_page(self, url:str):
        self.driver.get(url)
        return self

    def click(self, locator:tuple):
        element = self.driver.find_element(locator[0], locator[1])
        element.click()

    def is_visible(self):
        condition = EC.visibility_of_element_located(self)
        return bool(condition)

    def is_clickable(self):
        condition = EC.element_to_be_clickable(self)
        return bool(condition)