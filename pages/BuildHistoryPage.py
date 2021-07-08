from config.TestData import TestData as TD
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By



class BuildHistoryPage(BasePage):
    TITLE = 'Build History of Jenkins'
    BUILD_HISTORY_ITEM = (By.XPATH, '//a[@TITLE1="Build History"]')
    BHP_HREF = "view/all/builds"
    PAGE_URL = TD.BASE_URL + BHP_HREF
    TITLE1 = "Build History"
    BHPAGE_IMAGE= (By.XPATH, '//*[@id="main-panel"]/h1/img')
    TITLE_= (By.XPATH, '//*[contains(text(),"of Jenkins")]')
    SUBTITLE_= (By.XPATH, "//*[contains(text(),' is not guaranteed')]")
    PROJECT_STATUS_BUTTN= (By.XPATH, '//*[@id="projectStatus"]/tbody/tr/th[2]/a')
    BHP_TABLE_HEADER = (By.XPATH, "//table[contains(@class,'sortable pane bigtable')]")
    BHP_TABLE_HEADER1 = (By.XPATH, '//*[@id="timeline-band-0"]')
    LEGEND_BTN =(By.XPATH, "//*[@id='rss - bar']/a")
    ATOM_FEED_FORALL= (By.XPATH, '//*[@id="rss - bar"]/span[1]/a/span[2]')
    ATOM_FEED_FORFAILURES = (By.XPATH, ' "rss-bar"] / span[1] / a / span[2]')
    ATOM_FEED_FOR_LIST_BUILDS = (By.XPATH, '// *[ @ id = "rss-bar"] / span[3] / a / span[2]')
    REST_API = (By.XPATH, "//*[@id='jenkins']/footer/div/div/div[2]/a")
    JENKINS_VERS_NUMBER = (By.XPATH, '//*[@id="jenkins"]/footer/div/div/div[3]/a')

    def __init__(self, driver):
        super(BuildHistoryPage, self).__init__(driver)

    def get_currenturl(self):
        return self.driver.current_url


