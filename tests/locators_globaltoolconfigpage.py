from selenium.webdriver.common.by import By
from config.TestData import TestData

class NavigatetoGlobToolConfigLocators:
    DASHBOARD_LINK = (By.XPATH, "//a[text()='Dashboard']")
    PULLDOWN_ARROW = (By.ID, 'menuSelector')
    MANAGE_JENKINS_SUBMENU = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'manage')]"))
    GLOBTOOLGONG_SUBMENU = (By.XPATH, '//a[contains(text(),"Global Tool Configuration")]')
    PAGE_TITLE = (By.XPATH, '//h1[text()="Global Tool Configuration"]')

class HeadersLocators:
    BACK_ARROW = (By.XPATH, '//a[@title="Back to Dashboard"]')
    MANAGE_JENKINS_BUTTON = (By.XPATH, '//a[@title="Manage Jenkins"]')
    PAGE_TITLE = (By.XPATH, '//h1[text()="Global Tool Configuration"]')
    HEADER_SECTION = (By.XPATH, '//div[text()= "Maven Configuration"]')
    HEADER_PROVIDER = (By.XPATH, '//*[contains(text(), "Default settings provider")]')
    HEADER_GLOB_PROVIDER = (By.XPATH, '//*[contains(text(), "Default global settings provider")]')
    HEADER_JDK = (By.XPATH, '//*[text() = "JDK"]')
    HEADER_JDK_INSTALL = (By.XPATH, '//*[text() = "JDK installations"]')
    HEADER_GIT = (By.XPATH, '//*[@class="section-header"][text() = "Git"]')
    HEADER_GIT_INSTALL = (By.XPATH, '//*[text() = "Git installations"]')
    HEADER_GIT_SMALL = (By.XPATH, '//*[@class= "dd-handle"]')
    DEFAULT_FIELD = (By.XPATH, '//*[@name= "_.name"]')
    HEADER_PATH = (By.XPATH, '//*[text() = "Path to Git executable"]')
    GIT_FIELD = (By.XPATH, '//*[@name = "_.home"]')
    HEADER_INTALL_AUTO = (By.XPATH, '//*[text() = "Install automatically"]')
    HEADER_GRADLE = (By.XPATH, '//*[text() = "Gradle"]')
    HEADER_GRADLE_INSTALL = (By.XPATH, '//*[text() = "Gradle installations"]')
    HEADER_ANT = (By.XPATH, '//*[text() = "Ant"]')
    HEADER_ANT_INSTALL = (By.XPATH, '//*[text() = "Ant installations"]')
    HEADER_MAVEN = (By.XPATH, '//*[text() = "Maven"]')
    HEADER_MAVEN_INSTALL = (By.XPATH, '//*[text() = "Maven installations"]')

    locators_globtoolpage_all = [BACK_ARROW, MANAGE_JENKINS_BUTTON, PAGE_TITLE, HEADER_SECTION, HEADER_PROVIDER,
                                 HEADER_GLOB_PROVIDER, HEADER_JDK, HEADER_JDK_INSTALL, HEADER_GIT, HEADER_GIT_INSTALL,
                                 HEADER_GIT_SMALL, DEFAULT_FIELD, HEADER_PATH, GIT_FIELD, HEADER_INTALL_AUTO,
                                 HEADER_GRADLE, HEADER_GRADLE_INSTALL, HEADER_ANT, HEADER_ANT_INSTALL, HEADER_MAVEN,
                                 HEADER_MAVEN_INSTALL]
    ids_globtoolpage_all = ['BACK_ARROW', 'MANAGE_JENKINS_BUTTON', 'PAGE_TITLE', 'HEADER_SECTION', 'HEADER_PROVIDER',
                            'HEADER_GLOB_PROVIDER', 'HEADER_JDK', 'HEADER_JDK_INSTALL', 'HEADER_GIT',
                            'HEADER_GIT_INSTALL',
                            'HEADER_GIT_SMALL', 'DEFAULT_FIELD', 'HEADER_PATH', 'GIT_FIELD', 'HEADER_INTALL_AUTO',
                            'HEADER_GRADLE', 'HEADER_GRADLE_INSTALL', 'HEADER_ANT', 'HEADER_ANT_INSTALL',
                            'HEADER_MAVEN',
                            'HEADER_MAVEN_INSTALL']

class ButtonLocators:
    ADD_JDK = (By.CSS_SELECTOR, '#yui-gen6-button')
    DELETE_GIT = (By.CSS_SELECTOR, '#yui-gen10-button')
    ADD_GRADLE = (By.CSS_SELECTOR, '#yui-gen7-button')
    ADD_ANT = (By.CSS_SELECTOR, '#yui-gen8-button')
    ADD_MAVEN =(By.CSS_SELECTOR, '#yui-gen9-button')
    SAVE = (By.CSS_SELECTOR, '#yui-gen11-button')
    APPLY = (By.CSS_SELECTOR, '#yui-gen5-button')

    locators_buttons = [ADD_JDK, DELETE_GIT, ADD_GRADLE, ADD_ANT, ADD_MAVEN, SAVE, APPLY]

    ids_buttons = ['ADD_JDK', 'DELETE_GIT', 'ADD_GRADLE', 'ADD_ANT', 'ADD_MAVEN', 'SAVE','APPLY']



class Urllocators:
    URL_GLOBAL = TestData.BASE_URL + 'configureTools/'