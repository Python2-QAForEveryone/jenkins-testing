from config.TestData import TestData as TD
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By



class BuildHistoryPage(BasePage):
    URL_BUILD_HISTORY = TD.BASE_URL + 'view/all/builds'
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
    CHART_BUILD1=(By.XPATH, '//*[@id="label-tl-0-1-e1"]')
    CHART_TOOLTIP1= (By.XPATH, '//*[@id="jenkins"]/div[5]/div/div[9]/div/div[3]')
    CONSOLE_OUTPUT_PICTURE_LINK =(By.XPATH, '//*[@id="projectStatus"]/tbody/tr[2]/td[5]/a/img')
    CONSOLE_OUTPUT_PAGE=(By.XPATH, '//*[@id="main-panel"]/pre')
    FIRST_IN_LIST_OF_BUILDS=(By.XPATH, '//*[@id="projectStatus"]/tbody/tr[2]/td[2]')
    LIST_OF_BUILDS = (By.XPATH, '//*[@id="projectStatus"][1]')
    BUILD_PART1 = '//*[@id="job_'
    BUILD_PART2= ']/td[3]'


    def __init__(self, driver):
        super(BuildHistoryPage, self).__init__(driver)

    def get_list_builded_jobs(self, name):
        BUILDED_JOB = (By.XPATH, f'//a[@href="/job/{name}/"]')
        lst = self.get_elements(BUILDED_JOB)
        return lst

    def get_first_name_in_list(self, name):
        return By.XPATH, f'//*[@id="job_{name}"]/td[3]'

    def find_build_in_the_list(self,name):
        return (By.XPATH, f'//a[@href="job/{name}/"]')

    def get_console_output_from_the_list(self, name):
        return (By.XPATH, f'//a[@href="/job/{name}/1/console"]')

