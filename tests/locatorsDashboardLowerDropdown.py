from selenium.webdriver.common.by import By

from config.TestData import TestData


class DashboardLowerDropdownPageLocators:
    DASHBOARD_LINK = (By.XPATH, "//a[text()='Dashboard']")
    MENU_SELECTOR = (By.ID, 'menuSelector')


class DashboardLowerDropdownLocators:
    NEW_ITEM = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'newJob')]"))
    PEOPLE = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'People')]"))
    BUILD_HISTORY = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'builds')]"))
    MANAGE_JENKINS = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'manage')]"))
    MY_VIEWS = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'my-views')]"))
    LOCKABLE_RESOURCES = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'lockable-resources')]"))
    NEW_VIEW = (By.XPATH, ("//li[contains(@id,'yui-gen')]/a[contains(@href,'newView')]"))

    locators_for_dropdown = [NEW_ITEM, PEOPLE, BUILD_HISTORY, MANAGE_JENKINS, MY_VIEWS, LOCKABLE_RESOURCES, NEW_VIEW]


class ManageJenkinsDropdownLocators:
    CONFIGURE_SYSTEM = (By.XPATH, "(//li[@class='yuimenuitem']/a[contains(@href, 'configure')])[1]")
    GLOBAL_TOOL_CONFIGURATION = (By.XPATH, "//li[@class='yuimenuitem']/a[contains(@href, 'configureTools')]")
    MANAGE_PLUGINS = (By.XPATH, "//li[@class='yuimenuitem']/a[contains(@href, 'pluginManager')]")
    MANAGE_NODES_AND_CLOUDS = (By.XPATH, "//li[@class='yuimenuitem']/a[contains(@href, 'computer')]")
    CONFIGURE_GLOBAL_SECURITY = (By.XPATH, "//li[@class='yuimenuitem']/a[contains(@href, 'configureSecurity')]")
    MANAGE_CREDENTIALS = (By.XPATH, "//li[@class='yuimenuitem']/a[contains(@href, 'credentials')]")
    CONFIGURE_CREDENTIAL_PROVIDERS = (By.XPATH, "//li[@class='yuimenuitem']/a[contains(@href, 'configureCredentials')]")
    MANAGE_USERS = (By.XPATH, "//li[contains(@class,'yuimenuitem')]/a[contains(@href, 'securityRealm')]")
    IN_PROCESS_SCRIPT_APPROVAL = (By.XPATH, "//li[@class='yuimenuitem']/a[contains(@href, 'scriptApproval')]")
    SYSTEM_INFORMATION = (By.XPATH, "//li[@class='yuimenuitem']/a[contains(@href, 'systemInfo')]")
    SYSTEM_LOG = (By.XPATH, "//li[@class='yuimenuitem']/a[contains(@href, 'log')]")
    LOAD_STATISTICS = (By.XPATH, "//li[@class='yuimenuitem']/a[contains(@href, 'load-statistics')]")
    ABOUT_JENKINS = (By.XPATH, "//li[@class='yuimenuitem']/a[contains(@href, 'about')]")
    MANAGE_OLD_DATA = (By.XPATH, "//li[@class='yuimenuitem']/a[contains(@href, 'administrativeMonitor')]")
    RELOAD_CONFIGURATION_FROM_DISC = (By.XPATH, "//li[@class='yuimenuitem']/a[contains(@href, 'about')]")
    JENKINS_CLI = (By.XPATH, "//li[@class='yuimenuitem']/a[contains(@href, 'cli')]")
    SCRIPT_CONSOLE = (By.XPATH, "(//li[contains(@class,'yuimenuitem')]/a[contains(@href, 'script')])[2]")
    PREPARE_FOR_SHUTDOWN = (By.XPATH, "//li[@class='yuimenuitem']/a[contains(@href, 'prepareShutdown')]")

    SCROLL_DOWN = (By.XPATH, "//div[@class='ft bottomscrollbar bottomscrollbar_disabled']")

    locators_for_manage_jenkins_dropdown = [CONFIGURE_SYSTEM, GLOBAL_TOOL_CONFIGURATION, MANAGE_PLUGINS,
                                            MANAGE_NODES_AND_CLOUDS, CONFIGURE_GLOBAL_SECURITY, MANAGE_CREDENTIALS,
                                            CONFIGURE_CREDENTIAL_PROVIDERS, MANAGE_USERS, IN_PROCESS_SCRIPT_APPROVAL,
                                            SYSTEM_INFORMATION, SYSTEM_LOG, LOAD_STATISTICS, ABOUT_JENKINS,
                                            MANAGE_OLD_DATA, RELOAD_CONFIGURATION_FROM_DISC, JENKINS_CLI,
                                            SCRIPT_CONSOLE]

