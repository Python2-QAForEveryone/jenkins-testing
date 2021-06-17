from pages.BasePage import BasePage


class PeoplePage(BasePage):
    TITLE = 'People - [Jenkins]'

    def __init__(self, driver):
        super().__init__(driver)
