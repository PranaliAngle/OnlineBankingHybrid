import time

import pytest
from selenium.webdriver.common.alert import Alert


from PageObject.Loginpage import Loginpage
from PageObject.Search_Customer import Search_Customer
from PageObject.delete_Customer import Delete_Customer
from Utilities.customLogger import LogGen
from Utilities.readProperties import Readconfig

class Test_005_Delete_Customer:
    baseURL = Readconfig.getApplictionURL()
    loginid = Readconfig.getUserId()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_Customer(self,setup):
        self.logger.info("********** Test_004_Edit_Customer **********")
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
        self.logger.info("***************** Start Searching Customer by name ***************")

        self.searchcust=Search_Customer(self.driver)
        self.searchcust.click_On_customer()
        self.searchcust.click_On_View_customer()
        self.searchcust.set_searchBox("Pavan123")
        time.sleep(3)


        self.logger.info("******** search Customer by Name Sucessful **********")
        self.delcust=Delete_Customer(self.driver)
        self.delcust.delete_customer()


        self.logger.info("************ Delete Customer Validation Started ************")
        # create alert object
        alert = Alert(self.driver)
        self.msg = alert.text
        # get alert text
        print(self.msg)

        # accept the alert
        alert.accept()
        self.logger.info(self.msg+"************ is accepted *************")
        time.sleep(5)

        # create alert object
        alert1 = Alert(self.driver)
        self.msg1 = alert1.text
        # get alert text
        print(self.msg1)
        # accept the alert
        alert1.accept()

        if "Customer record deleted successfully..." in self.msg1:

            assert True == True
            self.logger.info("*********** Delete Customer Test Passed ************")

            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Delete_Customer.png")

            assert True == False
            self.logger.error("******** Delete Customer Test Failed **********")
            self.driver.quit()


