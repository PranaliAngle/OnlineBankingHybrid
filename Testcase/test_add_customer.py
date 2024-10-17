import random
import string
import time

import pytest
from selenium.webdriver.common.alert import Alert

from PageObject.Add_Customer import Customer
from PageObject.Loginpage import Loginpage
from Utilities.customLogger import LogGen
from Utilities.readProperties import Readconfig


class Test_002_Add_Customer:

    baseURL = Readconfig.getApplictionURL()
    loginid = Readconfig.getUserId()
    password = Readconfig.getPassword()


    logger = LogGen.loggen()

    @pytest.mark.Sanity
    def test_Add_Customer(self,setup):
        self.logger.info("********** Test_001_Login_title **********")
        self.logger.info("********** Verifying_Staff_Login_Page_Title **********")

        # self.driver=webdriver.chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.clickOnStaffLoginLink()
        self.lp.setLoginId(self.loginid)
        self.lp.setPassword(self.password)
        self.lp.clickSignIn()
        self.logger.info("***************** Login Succesful ************")
        self.logger.info("***************** Starting Add Customer ***************")
        self.addcust=Customer(self.driver)
        self.addcust.click_On_customer()
        self.addcust.click_On_Add_Customer()
        time.sleep(3)
        self.logger.info("************ Providing customer Info *************")
        self.addcust.set_customer_firstname("Pavan")
        self.addcust.set_customer_lastname("Kumar")
        self.addcust.set_customer_loginid("Pavan123")
        self.addcust.set_account_password("Pavan123")
        self.addcust.set_confirm_login_password("Pavan123")
        self.addcust.set_transaction_password("Pavan123")
        self.addcust.set_confirm_transaction_password("Pavan123")
        self.addcust.set_mobile_no("1234567898")
        #self.email=self.random_generator()+"@gmail.com"
        #self.addcust.set_emailid(self.email)
        self.addcust.set_emailid("Pavan@gmail.com")
        self.addcust.set_adderss("Plot no 123,durganager")
        self.addcust.set_city("Pune")
        self.addcust.set_state("Maharashtra")
        self.addcust.set_account_status("Active")
        self.addcust.click_on_submit()
        time.sleep(5)
        self.logger.info("********** Saving Customer Info *********** ")
        #self.driver.quit()
        self.logger.info("************ Add Customer Validation Started ************")
        # create alert object
        alert = Alert(self.driver)
        self.msg=alert.text
        # get alert text
        print(self.msg)

        # accept the alert
        alert.accept()

        if "Customer record inserted successfully.." in self.msg:

            assert True==True
            self.logger.info("*********** Add Customer Test Passed ************")
            print(self.driver.title)
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Add_Customer.png")
            self.logger.error("******** Add Customer Test Failed **********")
            assert True==False
            self.driver.quit()



    def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
        return ''.join(random.choice(chars)for x in range(size))

