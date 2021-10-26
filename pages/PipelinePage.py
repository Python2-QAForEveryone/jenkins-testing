from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from config.TestData import TestData as TD

class PipelinePageLocators:
    PIPELINE_RADIO = (By.XPATH, '//*[@id="j-add-item-type-standalone-projects"]/ul/li[2]')
    SUBMIT_BTN = (By.XPATH, '//*[@id="ok-button"]')
    MENU_TASKS = (By.XPATH, '//*[@id="tasks"]')
    BUILD_NOW = (By.XPATH, "//*[contains(text(),'Build Now')]")
    BACK_TO_DASHBOARD = (By.XPATH, "//a[@title='Back to Dashboard']")
    TAB_PART1 = '//a[contains(text(),\"'
    TAB_PART2 = '\")]'
    URL_PIPELINE_PAGE = TD.BASE_URL + "job/"
    BUILDS_RECORDS = (By.XPATH, '//a[contains(@class, "tip model-link inside build-link display-name")]')
    CONSOLE_OUTPUT = (By.XPATH, '//*[@id="main-panel"]/h1/text()')
    BUILD_STATUS = (By.XPATH, "//table[@class='pane stripped']//tr[2]//a[@class='build-status-link']/span")
    CONSOLE_OUTPUT = (By.XPATH,"//pre")
    BACK_TO_PROJECT=(By.XPATH, '//a[@title="Back to Project"]')
    CREATE_PIPELINE_SAMPLES =(By.XPATH, '//*[@class="samples"]')
    BUILD_HELLO_WORLD= (By.XPATH,'(//option[@value="hello"])[1]')
    BUILD_STATUS = (By.XPATH, "//table[@class='pane stripped']//tr[2]//a[@class='build-status-link']/span")



    def locator_for_tab(self,  name):
        return (By.XPATH, PipelinePageLocators.TAB_PART1 + f'{name}' + PipelinePageLocators.TAB_PART2)


class PipelineConfigureLocators:
    SAVE_PIPELINE = (By.XPATH, '//*[@type="submit"]')
    MENU_ITEM_CONFIGURE = (By.XPATH, '//*[contains(text(),"Configure")]')
    BOX_DISABLE = (By.XPATH, '//*[@name="disable"]')
    BTN_SAVE = (By.XPATH, '//*[@name="Submit"]')


class PipelinePage(BasePage):
    def __init__(self, driver) -> object:
        super().__init__(driver)




