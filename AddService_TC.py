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
        #xpath, clicks on service
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[3]/a").click()
        time.sleep(3)
        #xpath, clicks on Add Service
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(3)
        elem = driver.find_element_by_id("id_cust_name")
        #elem.clear()
        elem.send_keys("Bill Davis")
        time.sleep(2)
        elem = driver.find_element_by_id("id_service_category")
        #elem.clear()
        elem.send_keys("Food Delivery/Catering")
        time.sleep(2)
        elem = driver.find_element_by_id("id_description")
        elem.clear()
        elem.send_keys("Sandwich Lunch and Beverages for 30 people")
        time.sleep(2)
        elem = driver.find_element_by_id("id_location")
        elem.clear()
        elem.send_keys("PKI240")
        time.sleep(2)
        elem = driver.find_element_by_id("id_service_charge")
        elem.clear()
        elem.send_keys("350")
        time.sleep(2)
        # xpath, clicks on Save
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(5)





    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

