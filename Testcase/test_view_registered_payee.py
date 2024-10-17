
import random
import string
import time

from selenium.webdriver.common.alert import Alert

from PageObject.Add_Customer import Customer
from PageObject.Loginpage import Loginpage
from PageObject.View_registered_payee import View_registered_payee
from Utilities.customLogger import LogGen
from Utilities.readProperties import Readconfig

class Test_006_View_registered_Payee:
    baseURL = Readconfig.getApplictionURL()
    loginid = Readconfig.getUserId()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()

    def test_view_registered_payee(self,setup):
        self.logger.info("********** Test_006_View_registered_Payee **********")
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

        self.viewpayee=View_registered_payee(self.driver)
        self.viewpayee.click_On_customer()
        self.viewpayee.click_On_View_registered_payee()
        self.viewpayee.set_searchBox("Amrith")
        time.sleep(5)
        self.logger.info("***************** searching cutomer is succesfull ***************")
        self.logger.info("***************** finding status of Customer ***************")
        self.status=self.viewpayee.check_status()
        print(self.status)
        if self.status==" Inactive":
            self.viewpayee.click_on_active()
            self.logger.info("************** Validation of test_view_registered_payee start ***************")

            # create alert object
            alert = Alert(self.driver)
            self.msg = alert.text
            # get alert text
            print(self.msg)

            # accept the alert
            alert.accept()

            if "Registered payee record updated successfully.." in self.msg:

                assert True == True
                self.logger.info("*********** view registered payee Test Passed ************")

                self.driver.quit()
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_View_registered_payee.png")
                self.logger.error("******** View registered payee Failed **********")
                assert True == False
                self.driver.quit()

        else:
            self.viewpayee.click_on_deactive()
            self.logger.info("************** Validation of test_view_registered_payee start ***************")

            # create alert object
            alert1 = Alert(self.driver)
            self.msg1 = alert1.text
            # get alert text
            print(self.msg1)

            # accept the alert
            alert1.accept()

            if "Registered payee record updated successfully.." in self.msg1:

                assert True == True
                self.logger.info("*********** view registered payee Test Passed ************")

                self.driver.quit()
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_View_registered_payee.png")
                self.logger.error("******** View registered payee Failed **********")
                assert True == False
                self.driver.quit()



