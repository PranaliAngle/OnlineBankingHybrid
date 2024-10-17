import time

from selenium.webdriver.common.alert import Alert

from PageObject.Add_Customer import Customer
from PageObject.Loan import Loan
from PageObject.Loginpage import Loginpage
from PageObject.View_Loan_Account import View_Loan_Account
from Utilities.customLogger import LogGen
from Utilities.readProperties import Readconfig

class Test_008_View_Loan_Account:
    baseURL = Readconfig.getApplictionURL()
    loginid = Readconfig.getUserId()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()

    def test_view_loan_account(self,setup):
        self.logger.info("********** Test_008_View_Loan_Account **********")


        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.clickOnStaffLoginLink()
        self.lp.setLoginId(self.loginid)




        self.lp.setPassword(self.password)
        self.lp.clickSignIn()
        self.logger.info("***************** Login Succesfull ************")


        self.loan=Loan(self.driver)
        self.loan.click_on_loan()
        self.viewloan=View_Loan_Account(self.driver)
        self.viewloan.click_On_view_acounts()
        self.viewloan.set_searchBox("Raj")
        self.viewloan.click_on_View()
        self.logger.info("************* Validation of View Loan Accounts Start ************")
        self.header=self.viewloan.get_header()
        print(self.header)
        if "Individual Loan Payment Details" == self.header:

            assert True == True
            self.logger.info("*********** View Loan Account Test Passed ************")

            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_View_loan_Account.png")
            self.logger.error("******** View Loan Account Test Failed **********")
            assert True == False
            self.driver.quit()









