from selenium.webdriver.common.by import By


class DashboardPageLocators:
    DASHBOARD_MENU_ANCHOR = (By.CSS_SELECTOR, 'a.breadcrumbBarAnchor')
    MENU_SELECTOR = (By.ID, 'menuSelector')
    RIGHT_ARROW_SELECTOR = (By.CLASS_NAME, 'children')
    RIGHT_ARROW_SELECTOR_ALL = (By.XPATH, '//a[@href="/view/all/"]')
    RIGHT_ARROW_SELECTOR_ALL_VISIBLE = (By.ID, 'breadcrumb-menu')
    TEXT_NEW_ITEM = (By.XPATH, '//a[@title="New Item"]')
    ICON_NEW_ITEM = (By.CSS_SELECTOR, 'img.icon-new-package')
    TEXT_PEOPLE = (By.CSS_SELECTOR, 'a[title~=People]')
    ICON_PEOPLE = (By.XPATH, '//a[@title="People"]/span/img')
    TEXT_BUILD_HISTORY = (By.CSS_SELECTOR, 'a[title~=History]')
    ICON_BUILD_HISTORY = (By.CSS_SELECTOR, 'img.icon-notepad.icon-md')
    TEXT_MANAGE_JENKINS = (By.CSS_SELECTOR, 'a[title~=Manage]')
    ICON_MANAGE_JENKINS = (By.CSS_SELECTOR, 'img.icon-gear2')
    TEXT_MY_VIEWS = (By.CSS_SELECTOR, 'a[title~=Views]')
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
    EDIT_DESCRIPTION_LINK = (By.ID, 'description-link')
    ADD_DESCRIPTION_ICON = (By.CSS_SELECTOR, 'img.icon-notepad.icon-sm')
    DIV_DESCRIPTION = (By.ID, 'description')


class FooterLocators:
    FOOTER_REST_API = (By.CLASS_NAME, 'rest_api')
    FOOTER_VERSION = (By.CLASS_NAME, 'jenkins_ver')
    locators_for_footer = [FOOTER_REST_API, FOOTER_VERSION]


class URLLocators:
    URL_NEW_ITEM = 'http://localhost:8080/view/all/newJob'
    URL_PEOPLE = 'http://localhost:8080/asynchPeople/'
    URL_BUILD_HISTORY = 'http://localhost:8080/view/all/builds'
    URL_MANAGE_JENKINS = 'http://localhost:8080/manage'
    URL_MY_VIEW = 'http://localhost:8080/me/my-views/view/all/'
    URL_LOCKABLE_RESOURCES = 'http://localhost:8080/lockable-resources/'
    URL_NEW_VIEW = 'http://localhost:8080/newView'
    URL_FOOTER_REST_API = 'http://localhost:8080/api/'
    URL_FOOTER_VERSION = 'https://www.jenkins.io/'

class Titles:
    TITLE_DASHBOARD_PAGE = 'Dashboard [Jenkins]'
    TITLE_NEW_ITEM = 'New Item [Jenkins]'