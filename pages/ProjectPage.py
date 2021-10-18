from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from config.TestData import TestData as TD
from pages.DashboardPage import DashboardPageLocators, DashboardPage
from pages.ManageUserPage import ManageUserPage
from pages.NewItemPage import NewItemPageLocators


class ProjectPageLocators:
    PROJECT_NAME = (By.XPATH, '//h1')
    DELETE_PROJECT = (By.XPATH, '//a/span[contains(text(),"Delete")]')
    DISABLE_PROJECT_BUTTON = (By.XPATH, '//button[text()="Disable Project"]')
    ENABLE_PROJECT_BUTTON = (By.XPATH, '// button[text() = "Enable"]')
    DISABLE_PROJECT_WARNING = (By.XPATH, "//div[@class='warning']")
    ADD_DESCRIPTION_BUTTON = (By.ID, "description-link")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[@name='description']")
    SUBMIT_DESCRIPTION_BUTTON = (By.XPATH, "//button[text()='Submit']")
    DESCRIPTION = (By.XPATH, f"//div[@id='description']/div[1]")
    RENAME = (By.XPATH, "//span[text()='Rename']")
    NEW_NAME = (By.XPATH, "//input[@name='newName']")
    RENAME_BUTTON = (By.XPATH, "//button[text()='Rename']")
    BUILD_NOW = (By.XPATH, "//a[@title='Build Now']//span[2]")
    CONFIGURE = (By.XPATH, "//a[@title='Configure']//span[2]")
    BUILD_HISTORY_JOBS = (By.XPATH, '//tr[contains(@class, "build-row multi-line")]')
    BUILD_SUCCESS_JOBS = (By.XPATH, '//a[@class="build-status-link"]')
    BUILD_SUCCESS_LAST_JOB = (By.XPATH, '//td[@class="build-row-cell"][1]//a[@class="build-status-link"]')
    BUILD_LAST_JOB_BY_TEXT = (By.XPATH, '//a[contains(@class, "display-name")][1]')
    COUNT_OF_BUILD_HISTORY = (By.XPATH, '//table[@class="pane stripped"]//tr')
    CANCEL_BUILD = (By.XPATH, "//table[@class='pane stripped']//tr[2]//div[@class='build-stop']/a")
    BUILD_STATUS = (By.XPATH, "//table[@class='pane stripped']//tr[2]//a[@class='build-status-link']/img")
    BUILD_STATUS_CANCELLED = (By.XPATH, "//a[@class='build-status-link']/img[@title='Aborted > Console Output']")
    FIRST_BUILD = (
        By.XPATH,
        "//div[@id='buildHistory']//table[@class='pane stripped']//div[@class='pane build-name']//a[text()='#1']")
    WORKSPACE = (By.XPATH, "//a[@title='Workspace']//span[2]")


class ProjectPage(BasePage):
    """
    initialized driver
    added moving to the BasePage after log in
    """

    def __init__(self, driver):
        super().__init__(driver)

    def create_new_default_job(self, name, type_of_project):
        """
        create new job Freestyle project
        :return:
        """

        driver = DashboardPage(self.driver)
        driver.click(DashboardPageLocators.TEXT_NEW_ITEM)
        driver.do_send_keys(NewItemPageLocators.ENTER_AN_ITEM_NAME, name)
        driver.click(type_of_project)
        driver.get_wait_is_clickable(NewItemPageLocators.OK_BUTTON)
        driver.click(NewItemPageLocators.OK_BUTTON)

        return name

    def click_save_button_into_project(self, name):
        """
        click on the Save button into projects
        :return:
        """
        URL_JOB_FOR_SAVE = TD.BASE_URL + f'job/{name}/configure'

        driver = ProjectPage(self.driver)
        driver.go_to_page(URL_JOB_FOR_SAVE)
        driver.get_wait(NewItemPageLocators.SAVE_BUTTON)
        driver.click(NewItemPageLocators.SAVE_BUTTON)

    def delete_job(self, name):
        """
        delete job from list
        :param name:
        :return:
        """
        URL_JOB_FOR_DELETE = TD.BASE_URL + f'job/{name}/'

        driver = ProjectPage(self.driver)
        driver.go_to_page(URL_JOB_FOR_DELETE)
        driver.click(ManageUserPage.JOB_DELETE_PROJECT)
        driver.get_wait_for_alert()
        driver.accept_alert()
        driver.get_wait(DashboardPageLocators.TEXT_NEW_ITEM)

    def get_url_job(self, name):
        return TD.BASE_URL + f'job/{name}'

    def get_url_configure_of_job(self, name):
        return TD.BASE_URL + f'job/{name}/configure'
