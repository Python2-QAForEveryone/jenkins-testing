from config.TestData import TestData as TD
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By



class BuildHistoryPage(BasePage):
    TITLE = 'Build History of Jenkins'
    BUILD_History_item = (By.XPATH, '//a[@title="Build History"]')
    href = "view/all/builds"
    page_url = TD.BASE_URL+href
    title = "Build History"
    pict= (By.XPATH, '//*[@id="main-panel"]/h1/img')
    title_= (By.XPATH, '//*[contains(text(),"of Jenkins")]')
    subtitl_= (By.XPATH, "//*[contains(text(),' is not guaranteed')]")
    header_btn1= (By.XPATH, '//*[@id="projectStatus"]/tbody/tr/th[2]/a')
    # role=generic
    tble_header = (By.XPATH, "//table[contains(@class,'sortable pane bigtable')]")
    # its a link
    legend_btn =(By.XPATH, "//*[@id='rss - bar']/a")
    # role=generic
    Atom_feed_forall= (By.XPATH,'//*[@id="rss - bar"]/span[1]/a/span[2]')
    # role=generic
    Atom_feed_forfailures = (By.XPATH, ' "rss-bar"] / span[1] / a / span[2]')
    # role=generic
    Atom_feed_for_ltst_builds = (By.XPATH,'// *[ @ id = "rss-bar"] / span[3] / a / span[2]')
    # its a link
    Rest_API = (By.XPATH, "//*[@id='jenkins']/footer/div/div/div[2]/a")
    # its a link
    jnkins_version_number = (By.XPATH,'//*[@id="jenkins"]/footer/div/div/div[3]/a')

    def __init__(self, driver):
        super(BuildHistoryPage, self).__init__(driver)

    def get_currenturl(self):
        return self.driver.current_url


