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
    CONSOLE_OUTPUT_AFTER_BUILD = (By.XPATH, '//pre[@class="console-output"]')
    AFTER_BUILD_WORKSPACE_PAGE_TITLE = (By.XPATH, '//h1')

    SELECTION_SOURCE_CODE = \
        (By.XPATH, '//div[contains(@class, "config-section-activator config_source_code_management")]')
    TITLE_SOURCE_CODE = (By.XPATH, '//div[@title="Source Code Management"]')

    SELECTION_BUILD_TRIGGERS = (
        By.XPATH, '//div[contains(@class, "config-section-activator config_build_triggers")]')
    TITLE_BUILD_TRIGGERS = (By.XPATH, '//div[@title="Build Triggers"]')

    SELECTION_BUILD_ENVIRONMENT = (
        By.XPATH, '//div[contains(@class, "config-section-activator config_build_environment")]')
    TITLE_BUILD_ENVIRONMENT = (By.XPATH, '//div[@title="Build Environment"]')

    SELECTION_BUILD = (
        By.XPATH, '//div[contains(@class, "config-section-activator config_build")]')
    TITLE_BUILD = (By.XPATH, '//div[@title="Build"]')

    SELECTION_POST_BUILD_ACTIONS = (
        By.XPATH, '//div[contains(@class, "config-section-activator config_post_build_actions")]')
    TITLE_POST_BUILD_ACTIONS = (By.XPATH, '//div[@title="Post-build Actions"]')

    verify_works_tabs = [(SELECTION_GENERAL, TEXTAREA_DESCRIPTION),
                         (SELECTION_SOURCE_CODE, TITLE_SOURCE_CODE),
                         (SELECTION_BUILD_TRIGGERS, TITLE_BUILD_TRIGGERS),
                         (SELECTION_BUILD_ENVIRONMENT, TITLE_BUILD_ENVIRONMENT),
                         (SELECTION_BUILD, TITLE_BUILD),
                         (SELECTION_POST_BUILD_ACTIONS, TITLE_POST_BUILD_ACTIONS)]
