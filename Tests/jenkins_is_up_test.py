import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestJenkinsTitle:

    def test_jenkins_title(self):
        self.driver.get("http://localhost:8080/")
        # WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'j_username')))
        print("*************************************")
        # # print(os.environ)
        # InitialAdminPassword = os.environ.get('InitialAdminPassword')
        # print(InitialAdminPassword)
        # # asd= os.system('docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword')
        # # with open ('/home/travis/apt-get-update.log', "r") as file:
        # #     print(file.read())
        # #
        # print("*************************************")
        # self.driver.find_element_by_id('security-token').send_keys(os.system('docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword'))
        # time.sleep(5)
        # print(self.driver.find_element_by_xpath('//*[@id="main-panel"]/form/div[1]/div/div/div/div[2]/div/p[2]/small/code').text)
        print(self.driver.title, "!!!!!!!!!!!!!!!!!!")
        # with open("/var/jenkins_home/secrets/initialAdminPassword", "r") as file:
        #     jenkins_password = file.read()
        # print(jenkins_password)
