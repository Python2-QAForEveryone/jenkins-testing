from pages.BasePage import BasePage

class GlobalToolConfiguration(BasePage):
    TITLE = 'Global Tool Configuration'

    def __init__(self, driver):
        super().__init__(driver)
