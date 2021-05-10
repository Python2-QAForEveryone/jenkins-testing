from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestJenkinsIsUp:

    def test_jenkins_is_up(self):
        self.driver.get("http://localhost:8080/")
        print("*************************************")
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'j_username')))
            print("PASS")
        except:
            print("Not found")
        print(self.driver.title, "!!!!!!!!!!!!!!!!!!")
