import time

from PageObject.Loginpage import Loginpage
from PageObject.Withdraw_Money import Withdraw_Money
from Utilities.customLogger import LogGen
from Utilities.readProperties import Readconfig

class Test_010_Withdraw_Money:
    baseURL = Readconfig.getApplictionURL()
    loginid = Readconfig.getUserId()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()

    def test_withdraw_money(self,setup):
        self.logger.info("********** Test_010_Withdraw_Money **********")


        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("************* Login Start ********************")
        self.lp = Loginpage(self.driver)
        self.lp.clickOnStaffLoginLink()
        self.lp.setLoginId(self.loginid)
        self.lp.setPassword(self.password)
        self.lp.clickSignIn()
        self.logger.info("***************** Login Succesfull ************")
        self.logger.info("***************** Proving info to Withdraw Money  ********")
        self.withm=Withdraw_Money(self.driver)

        self.withm.click_on_transaction_linked_text()
        self.withm.click_on_deposit_money_linked_text()
        self.withm.set_account_number("117501000811409")
        self.withm.wait()
        #self.depom.set_acc_no("117501000811409")
        self.withm.set_amount(10)

        self.withm.set_perticulers("abcdefg")
        self.withm.click_on_submit()

        self.logger.info("******************** Save Withdraw Money ************ ")
        self.msg = self.withm.withdraw_money_alert()
        self.logger.info("************ Withdraw Money Validation Started ************")

        if "Withdrawal Successful..." in self.msg:

            assert True == True
            self.logger.info("*********** Withdraw Money Test Passed ************")
            print(self.driver.title)
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Withdraw_Money.png")
            self.logger.error("******** Withdraw Money Test Failed **********")
            assert True == False
            self.driver.quit()
