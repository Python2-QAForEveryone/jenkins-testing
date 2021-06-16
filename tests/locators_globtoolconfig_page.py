from selenium.webdriver.common.by import By
from config.TestData import TestData

class NavigatetoGlobToolConfigLocators:
    PULLDOWN_ARROW = (By.id, 'menuSelector')
    MANAGE_JENKINS_SUBMENU = (By.XPATH, '//a[contains(text(),"Manage Jenkins")]')
    GLOBTOOLGONG_SUBMENU = (By.XPATH, '//a[contains(text(),"Global Tool Configuration")]')

class GlobToolConfigPageLocators:
    BACK_ARROW = (By.XPATH, '//a[@title="Back to Dashboard"]')
    MANAGE_JENKINS_BUTTON = (By.XPATH, '//a[@title="Manage Jenkins"]')





