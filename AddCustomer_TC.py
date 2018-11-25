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
        #xpath, clicks on view details button for available beds
        #elem = driver.find_element_by_xpath("/html/body/div/div/div/div/form/p[4]/input").click()
        #time.sleep(2)
        #xpath, clicks on view details of customer
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
        time.sleep(3)
        #xpath, clicks on Add Customer
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(3)
        elem = driver.find_element_by_id("id_cust_name")
        elem.clear()
        elem.send_keys("Lakshya")
        time.sleep(2)
        elem = driver.find_element_by_id("id_organization")
        elem.clear()
        elem.send_keys("Economics")
        time.sleep(2)
        elem = driver.find_element_by_id("id_role")
        elem.clear()
        elem.send_keys("Professor")
        time.sleep(2)
        elem = driver.find_element_by_id("id_bldgroom")
        elem.clear()
        elem.send_keys("PKI240")
        time.sleep(2)
        elem = driver.find_element_by_id("id_account_number")
        elem.clear()
        elem.send_keys("150")
        time.sleep(2)
        elem = driver.find_element_by_id("id_address")
        elem.clear()
        elem.send_keys("124 Q st")
        time.sleep(2)
        elem = driver.find_element_by_id("id_city")
        elem.clear()
        elem.send_keys("Omaha")
        time.sleep(2)
        elem = driver.find_element_by_id("id_state")
        elem.clear()
        elem.send_keys("NE")
        time.sleep(2)
        elem = driver.find_element_by_id("id_zipcode")
        elem.clear()
        elem.send_keys("68135")
        time.sleep(2)
        elem = driver.find_element_by_id("id_email")
        elem.clear()
        elem.send_keys("ljha@gmail.com")
        time.sleep(2)
        elem = driver.find_element_by_id("id_phone_number")
        elem.clear()
        elem.send_keys("4023337890")
        time.sleep(2)
        # xpath, clicks on Save
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/table/tbody/tr/td[1]/button").click()
        time.sleep(5)
        # xpath, clicks on dropdown
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        time.sleep(3)
        # xpath, clicks on logout
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/ul/li[1]/a").click()
        time.sleep(3)




    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

