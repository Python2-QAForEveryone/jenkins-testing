from pages.BasePage import BasePage


class GlobalToolConfigPage(BasePage):

    TITLE = 'Global Tool Configuration [Jenkins]'

    def __init__(self, driver):
        super().__init__(driver)