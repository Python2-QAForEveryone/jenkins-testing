from pages.BasePage import BasePage
from config.TestData import TestData
from selenium.webdriver.common.by import By


class FreestylePage(BasePage):
    """
    initialized driver
    added moving to the BasePage after log in
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_page(URLLocators.URL_FREESTYLE_CREATE)


class URLLocators:
    URL_FREESTYLE_CREATE = TestData.BASE_URL + 'view/all/newJob'


class FreestylePageLocators:
    SELECTION_GENERAL = (By.XPATH, '//div[contains(@class, "config-section-activator config_general")]')
    TEXTAREA_DESCRIPTION = (By.XPATH, '//textarea[@name="description"]')
    CHECKBOX_DISABLE_THIS_PROJECT = (By.XPATH, "//label[text()='Disable this project']/../input")

    SELECTION_SOURCE_CODE = \
        (By.XPATH, '//div[contains(@class, "config-section-activator config_source_code_management")]')
    TITLE_SOURCE_CODE = (By.XPATH, '//div[@title="Source Code Management"]')

    SELECTION_BUILD_TRIGGERS = (
        By.XPATH, '//div[contains(@class, "config-section-activator config_build_triggers")]')
    TITLE_BUILD_TRIGGERS = (By.XPATH, '//div[@title="Build Triggers"]')

    SELECTION_BUILD_ENVIRONMENT = (
        By.XPATH, '//div[contains(@class, "config-section-activator config_build_environment")]')
    TITLE_BUILD_ENVIRONMENT = (By.XPATH, '//div[@title="Build Environment"]')
    CHECKBOX_ADD_TIMESTAMPS_TO_CONSOLE_OUTPUT = \
        (By.XPATH, '//input[@name="hudson-plugins-timestamper-TimestamperBuildWrapper"]')

    SELECTION_BUILD = (
        By.XPATH, '//div[contains(@class, "config-section-activator config_build")]')
    TITLE_BUILD = (By.XPATH, '//div[@title="Build"]')
    BUTTON_ADD_BUILD_STEPS = (By.ID, 'yui-gen13-button')
    OPTION_EXECUTE_WINDOWS_COMMAND = \
        (By.XPATH, '//div[@id="yui-gen14"]//a[text()="Execute Windows batch command"]')
    TEXTAREA_COMMAND = (By.XPATH, '//textarea[@name="command"]')

    SELECTION_POST_BUILD_ACTIONS = (
        By.XPATH, '//div[contains(@class, "config-section-activator config_post_build_actions")]')
    TITLE_POST_BUILD_ACTIONS = (By.XPATH, '//div[@title="Post-build Actions"]')
    BUTTON_ADD_POST_BUILD_ACTION = (By.ID, "yui-gen15-button")
    OPTION_EDITABLE_EMAIL_NOTIFICATION = \
        (By.XPATH, '//div[@id="yui-gen16"]//a[text()="Editable Email Notification"]')
    EDITABLE_AREA = (By.XPATH, '//div[@class="dd-handle"]/b[text()="Editable Email Notification"]')

    verify_works_tabs = [(SELECTION_GENERAL, TEXTAREA_DESCRIPTION),
                         (SELECTION_SOURCE_CODE, TITLE_SOURCE_CODE),
                         (SELECTION_BUILD_TRIGGERS, TITLE_BUILD_TRIGGERS),
                         (SELECTION_BUILD_ENVIRONMENT, TITLE_BUILD_ENVIRONMENT),
                         (SELECTION_BUILD, TITLE_BUILD),
                         (SELECTION_POST_BUILD_ACTIONS, TITLE_POST_BUILD_ACTIONS)]
