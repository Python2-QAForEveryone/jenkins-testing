from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ConsoleOutputPage(BasePage):
    LINES_WITH_TIMESTAMPS = (By.XPATH, '//pre[@class="console-output"]/span[@class="timestamp"]')
    TITLE = (By.TAG_NAME, 'h1')
    LINES_TEXT = (By.XPATH, '//pre[@class="console-output"]')
    CONSOLE_OUTPUT_AFTER_BUILD = (By.XPATH, '//pre[@class="console-output"]')

    def __init__(self, driver):
        super(ConsoleOutputPage, self).__init__(driver)

    def is_contains_text(self, lines, subtext):
        for line in lines:
            if line.__contains__(subtext):
                return True
        return False
