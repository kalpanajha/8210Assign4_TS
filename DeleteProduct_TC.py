import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class admin_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\Webdrivers/chromedriver.exe')

    def test_blog(self):
        user = "instructor"
        pwd = "8210login"
        driver = self.driver

        driver.get("http://kjhamishra.pythonanywhere.com/")
        time.sleep(3)

        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "Logged In"
        time.sleep(2)
        #xpath, clicks on view details of Product
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[3]/div/div/p[2]/a").click()
        time.sleep(3)
        # xpath, clicks on delete button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[3]/td[8]/a").click()
        time.sleep(3)
        driver.switch_to.alert.accept()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

