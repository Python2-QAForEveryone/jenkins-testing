from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class NewItemPageLocators:
    ENTER_AN_ITEM_NAME = (By.ID, 'name')
    ERROR_MESSAGE = (By.XPATH, "//div[@class='input-validation-message input-message-disabled']")
    OK_BUTTON = (By.XPATH, '//button[@type="submit"]')
    PIPELINE = (By.XPATH, '//li[@class="org_jenkinsci_plugins_workflow_job_WorkflowJob"]')
    MULTI_CONFIGURATION_PROJECT = (By.XPATH, '//li[@class="hudson_matrix_MatrixProject"]')
    SAVE_BUTTON = (By.XPATH, '//span[@name="Submit"]')


class NewItemPage(BasePage):
    """
    initialized driver
    added moving to the BasePage after log in
    """

    def __init__(self, driver):
        super().__init__(driver)

