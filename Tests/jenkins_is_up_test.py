import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestJenkinsTitle:

    def test_jenkins_title(self):
        self.driver.get("http://localhost:8080/")
        print("*************************************")
        print(self.driver.title, "!!!!!!!!!!!!!!!!!!")