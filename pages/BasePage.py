from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def go_to_page(self, url: str):
        self.driver.get(url)
        return self

    def click(self, locator: tuple):
        element = self.driver.find_element(locator[0], locator[1])
        element.click()

    def is_visible(self, locator: tuple):
        condition = EC.visibility_of_element_located(locator)
        element = WebDriverWait(self.driver, 2).until(condition)
        return bool(element)

    def is_clickable(self, locator: tuple):
        condition = EC.element_to_be_clickable(locator)
        element = WebDriverWait(self.driver, 2).until(condition)
        return bool(element)

    def get_element(self, locator):
        element = self.driver.find_element(locator[0], locator[1])
        return element

    def get_element_text(self, locator):
        condition = EC.visibility_of_element_located(locator)
        element = WebDriverWait(self.driver, 2).until(condition)
        return element.text

    def do_send_keys(self, locator, text):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locator)).sendKeys(text)
