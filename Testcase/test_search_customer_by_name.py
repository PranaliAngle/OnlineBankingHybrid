

import random
import string
import time

import pytest
from selenium.webdriver.common.alert import Alert

from PageObject.Add_Customer import Customer
from PageObject.Loginpage import Loginpage
from PageObject.Search_Customer import Search_Customer
from Utilities.customLogger import LogGen
from Utilities.readProperties import Readconfig

class Test_003_Search_Customer_By_Name:
    baseURL = Readconfig.getApplictionURL()
    loginid = Readconfig.getUserId()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()


    def test_search_Customer(self,setup):
        self.logger.info("********** Test_003_Search_Customer_by_Name **********")
        self.logger.info("********** Verifying_Search_customer **********")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.clickOnStaffLoginLink()
        self.lp.setLoginId(self.loginid)
        self.lp.setPassword(self.password)
        self.lp.clickSignIn()
        self.logger.info("***************** Login Succesfull ************")
        self.logger.info("***************** Start Searching Customer by Name ***************")

        self.searchcust=Search_Customer(self.driver)
        self.searchcust.click_On_customer()
        self.searchcust.click_On_View_customer()
        self.searchcust.set_searchBox("Raj")
        time.sleep(5)
        status=self.searchcust.search_customer_by_name("Raj")
        assert True==status
        self.logger.error("******** search Customer by Name Test Passed **********")
        time.sleep(3)
        self.driver.quit()

        self.driver.quit()
        if status==False:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_search_Customer_Name.png")
            self.logger.error("******** search Customer by Name Test Failed **********")
            self.driver.quit()





