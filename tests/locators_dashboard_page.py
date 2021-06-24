from selenium.webdriver.common.by import By

from config.TestData import TestData


class DashboardPageLocators:
    DASHBOARD_MENU_ANCHOR = (By.CSS_SELECTOR, 'a.breadcrumbBarAnchor')
    MENU_SELECTOR = (By.ID, 'menuSelector')
    RIGHT_ARROW = (By.XPATH, '//ul[@id="breadcrumbs"]/li[@class="children"]')
    RIGHT_ARROW_MENU = (By.XPATH, '//a[@href="/view/all/"]')
    RIGHT_ARROW_MENU_ICON = (By.XPATH, '//div[@id="breadcrumb-menu-target"]/div')
    TEXT_NEW_ITEM = (By.XPATH, '//a[@title="New Item"]')
    ICON_NEW_ITEM = (By.CSS_SELECTOR, 'img.icon-new-package')
    TEXT_PEOPLE = (By.CSS_SELECTOR, 'a[title~=People]')
    ICON_PEOPLE = (By.XPATH, '//a[@title="People"]/span/img')
    TEXT_BUILD_HISTORY = (By.CSS_SELECTOR, 'a[title~=History]')
    ICON_BUILD_HISTORY = (By.CSS_SELECTOR, 'img.icon-notepad.icon-md')
    TEXT_MANAGE_JENKINS = (By.XPATH, '//a[@href="/manage"]/span[text()="Manage Jenkins"]')
    ICON_MANAGE_JENKINS = (By.CSS_SELECTOR, 'img.icon-gear2')
    TEXT_MY_VIEWS = (By.XPATH, '//a[@href="/me/my-views"]/span[text()="My Views"]')
    ICON_MY_VIEWS = (By.XPATH, '//a[@title="My Views"]/span[1]/img')
    TEXT_LOCKABLE_RESOURCES = (By.CSS_SELECTOR, 'a[title~=Resources]')
    ICON_LOCKABLE_RESOURCES = (By.XPATH, '//a[@title="Lockable Resources"]/span/img')
    TEXT_NEW_VIEW = (By.XPATH, '//a[@title="New View"]')
    ICON_NEW_VIEW = (By.CSS_SELECTOR, 'img.icon-folder')

    locators_dashboard_all = [TEXT_NEW_ITEM, ICON_NEW_ITEM, TEXT_PEOPLE, ICON_PEOPLE,
                              TEXT_BUILD_HISTORY, ICON_BUILD_HISTORY, TEXT_MANAGE_JENKINS,
                              ICON_MANAGE_JENKINS, TEXT_MY_VIEWS, ICON_MY_VIEWS,
                              TEXT_LOCKABLE_RESOURCES, ICON_LOCKABLE_RESOURCES, TEXT_NEW_VIEW,
                              ICON_NEW_VIEW]
    ids_dashboard_all = ['TEXT_NEW_ITEM', 'ICON_NEW_ITEM', 'TEXT_PEOPLE', 'ICON_PEOPLE',
                              'TEXT_BUILD_HISTORY', 'ICON_BUILD_HISTORY', 'TEXT_MANAGE_JENKINS',
                              'ICON_MANAGE_JENKINS', 'TEXT_MY_VIEWS', 'ICON_MY_VIEWS',
                              'TEXT_LOCKABLE_RESOURCES', 'ICON_LOCKABLE_RESOURCES', 'TEXT_NEW_VIEW',
                              'ICON_NEW_VIEW']
    locators_dashboard_text_field = [TEXT_NEW_ITEM, TEXT_PEOPLE, TEXT_BUILD_HISTORY,
                                     TEXT_MANAGE_JENKINS, TEXT_MY_VIEWS, TEXT_LOCKABLE_RESOURCES,
                                     TEXT_NEW_VIEW]
    ids_dashboard_text_field = ['TEXT_NEW_ITEM', 'TEXT_PEOPLE', 'TEXT_BUILD_HISTORY',
                                     'TEXT_MANAGE_JENKINS', 'TEXT_MY_VIEWS', 'TEXT_LOCKABLE_RESOURCES',
                                     'TEXT_NEW_VIEW']

class BuildLocators:
    BUILD_QUEUE = (By.XPATH, '//span[text()="Build Queue"]')
    BUILD_EXECUTOR_STATUS = (By.XPATH, '//a[@href="/computer/"]')


class WelcomeLocators:
    CREATE_JOB = (By.XPATH, '//a[@href="newJob"]')
    SET_UP_AN_AGENT = (By.XPATH, '//a[@href="computer/new"]')
    CONFIGURE_A_CLOUD = (By.XPATH, '//a[@href="configureClouds"]')
    LEARN_MORE_ABOUT_DISTRIBUTED_BUILDS = (By.CSS_SELECTOR, 'a.content-block__link.content-block__help-link')


class AddDescriptionLocators:
    ADD_DESCRIPTION_LINK = (By.ID, 'description-link')
    ADD_DESCRIPTION_ICON = (By.CSS_SELECTOR, 'img.icon-notepad.icon-sm')
    DIV_DESCRIPTION = (By.ID, 'description')
    EDIT_DESCRIPTION_LINK = (By.ID, 'description-link')
    TEXTAREA_DESCRIPTION = (By.XPATH, '//textarea[@name="description"]')
    BUTTON_SUBMIT_DESCRIPTION = (By.ID, 'yui-gen1-button')
    TEXT_TO_DESCRIPTION = 'Copirate by Mirovich Mikhail'
    VERIFY_DESCRIPTION_TEXT = (By.XPATH, '//div[@id="description"]/div[1]')


class FooterLocators:
    FOOTER_REST_API = (By.CLASS_NAME, 'rest_api')
    FOOTER_VERSION = (By.XPATH, '//div[contains(@class, "jenkins_ver")]/a')
    locators_for_footer = [FOOTER_REST_API, FOOTER_VERSION]


class URLLocators:
    URL_RIGHT_ARROW = TestData.BASE_URL + 'view/all/'
    URL_NEW_ITEM = TestData.BASE_URL + 'view/all/newJob'
    URL_PEOPLE = TestData.BASE_URL + 'asynchPeople/'
    URL_BUILD_HISTORY = TestData.BASE_URL + 'view/all/builds'
    URL_MANAGE_JENKINS = TestData.BASE_URL + 'manage'
    URL_MY_VIEW = TestData.BASE_URL + 'me/my-views/view/all/'
    URL_LOCKABLE_RESOURCES = TestData.BASE_URL + 'lockable-resources/'
    URL_NEW_VIEW = TestData.BASE_URL + 'newView'
    URL_FOOTER_REST_API = TestData.BASE_URL + 'api/'
    URL_BUILD_EXECUTOR_STATUS = TestData.BASE_URL + 'computer/'
    URL_FOOTER_VERSION = 'https://www.jenkins.io/'

class Titles:
    TITLE_DASHBOARD_PAGE = 'Dashboard [Jenkins]'
    TITLE_NEW_ITEM = 'New Item [Jenkins]'

class EmptyStateBlock:
    WELCOME_TO_JENKINS = (By.XPATH, '//h1[text()="Welcome to Jenkins!"]')
    TEXT_UNDER_WELCOME = (By.XPATH, '//div[contains(@class, "empty-state-block")]/p')
    SECTION_TEXT_START = (By.XPATH, '//div[contains(@class, "empty-state-block")]/section[1]/h2')
    SECTION_TEXT_SET_UP = (By.XPATH, '//div[contains(@class, "empty-state-block")]/section[2]/h2')
    CREATE_JOB_TEXT = (By.XPATH, '//a[@href="newJob"]/span[text()="Create a job"]')
    CREATE_JOB_ARROW = (By.XPATH, '//a[@href="newJob"]/span[@class="trailing-icon"]')
    SET_UP_TEXT = (By.XPATH, '//a[@href="computer/new"]/span[text()="Set up an agent"]')
    SET_UP_ARROW = (By.XPATH, '//a[@href="computer/new"]/span[@class="trailing-icon"]')
    CONFIGURE_CLOUD_TEXT = (By.XPATH, '//a[@href="configureClouds"]/span[text()="Configure a cloud"]')
    CONFIGURE_CLOUD_ARROW = (By.XPATH, '//a[@href="configureClouds"]/span[@class="trailing-icon"]')
    LEARN_MORE_TEXT = (By.XPATH, '//a[@href="https://jenkins.io/redirect/distributed-builds"]/span[contains(text(), "Learn more")]')
    LEARN_MORE_SIGN = (By.XPATH, '//a[@href="https://jenkins.io/redirect/distributed-builds"]/span[@class="trailing-icon"]')

    locators_for_visible_dashboard = [WELCOME_TO_JENKINS, TEXT_UNDER_WELCOME, SECTION_TEXT_START, SECTION_TEXT_SET_UP,
                                      CREATE_JOB_TEXT, CREATE_JOB_ARROW, SET_UP_TEXT, SET_UP_ARROW, CONFIGURE_CLOUD_TEXT,
                                      CONFIGURE_CLOUD_ARROW, LEARN_MORE_TEXT, LEARN_MORE_SIGN]
    ids_for_visible_dashboard = ['WELCOME_TO_JENKINS', 'TEXT_UNDER_WELCOME', 'SECTION_TEXT_START', 'SECTION_TEXT_SET_UP',
                                 'CREATE_JOB_TEXT', 'CREATE_JOB_ARROW', 'SET_UP_TEXT', 'SET_UP_ARROW',
                                 'CONFIGURE_CLOUD_TEXT', 'CONFIGURE_CLOUD_ARROW', 'LEARN_MORE_TEXT', 'LEARN_MORE_SIGN']
    locators_for_clickable_dashboard = [CREATE_JOB_TEXT, CREATE_JOB_ARROW, SET_UP_TEXT, SET_UP_ARROW,
                                        CONFIGURE_CLOUD_TEXT, CONFIGURE_CLOUD_ARROW, LEARN_MORE_TEXT, LEARN_MORE_SIGN]
    ids_for_clickable_dashboard = ['CREATE_JOB_TEXT', 'CREATE_JOB_ARROW', 'SET_UP_TEXT', 'SET_UP_ARROW',
                                   'CONFIGURE_CLOUD_TEXT', 'CONFIGURE_CLOUD_ARROW', 'LEARN_MORE_TEXT', 'LEARN_MORE_SIGN']
