import random
import string
import time

from selenium.webdriver.common.alert import Alert

from PageObject.Add_Customer import Customer
from PageObject.Edit_Customer import Edit_Customer
from PageObject.Loginpage import Loginpage
from PageObject.Search_Customer import Search_Customer
from Utilities.customLogger import LogGen
from Utilities.readProperties import Readconfig

class Test_004_Edit_Customer:
    baseURL = Readconfig.getApplictionURL()
    loginid = Readconfig.getUserId()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()

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
        self.searchcust.set_searchBox("amrithbilawal")
        time.sleep(5)
        status=self.searchcust.search_customer_by_name("amrithbilawal")

        self.logger.info("******** search Customer by Name Sucessful **********")
        self.editcust=Edit_Customer(self.driver)
        self.editcust.edit_customer()
        self.logger.info("*********** Starting Edit Customer test")
        self.logger.info("*********** Providing Info to edit customer details *******")

        self.logger.info("************ Providing customer Info *************")
        #self.editcust.edit_customer_firstname("Pavan")
        self.editcust.edit_customer_lastname("Kumar")
        #self.editcust.edit_customer_loginid("Pavan123")
        #self.editcust.edit_account_password("Pavan123")
        #self.editcust.edit_confirm_login_password("Pavan123")
        #self.editcust.edit_transaction_password("Pavan123")
        #self.editcust.edit_confirm_transaction_password("Pavan123")
        #self.editcust.edit_mobile_no("1234567898")
        # self.email=self.random_generator()+"@gmail.com"
        # self.addcust.set_emailid(self.email)
        self.editcust.edit_emailid("Pavan@gmail.com")
        self.editcust.edit_adderss("Plot no 13,durganager")
        #self.editcust.edit_city("Pune")
        self.editcust.edit_state("Maharashtra")
        self.editcust.edit_account_status("Active")
        self.editcust.click_on_submit()
        self.logger.info("************ Add Customer Validation Started ************")
        # create alert object
        alert = Alert(self.driver)
        self.msg = alert.text
        # get alert text
        print(self.msg)

        # accept the alert
        alert.accept()

        if "Custer record updated successfully." in self.msg:

            assert True == True
            self.logger.info("*********** Edit Customer Test Passed ************")

            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Edit_Customer.png")
            self.logger.error("******** Edit Customer Test Failed **********")
            assert True == False
            self.driver.quit()










