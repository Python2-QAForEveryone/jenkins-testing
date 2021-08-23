from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class PipelinePageLocators:
    PIPELINE_RADIO = (By.XPATH, '//*[@id="j-add-item-type-standalone-projects"]/ul/li[2]')
    SUBMIT_BTN = (By.XPATH, '//*[@id="ok-button"]')
    MENU_TASKS = (By.XPATH, '//*[@id="tasks"]')
    BUILD_NOW = (By.XPATH, "//*[contains(text(),'Build Now')]")

class PipelineConfigureLocators:
    SAVE_PIPELINE = (By.XPATH, '//*[@type="submit"]')
    MENU_ITEM_CONFIGURE = (By.XPATH, '//*[contains(text(),"Configure")]')
    BOX_DISABLE = (By.XPATH, '//*[@name="disable"]')
    BTN_SAVE = (By.XPATH, '//*[@name="Submit"]')


class PipelinePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
