import time

from selenium.webdriver.common.alert import Alert

from PageObject.Loginpage import Loginpage
from PageObject.Deposit_Money import Deposit_Money
from Utilities.customLogger import LogGen
from Utilities.readProperties import Readconfig

class Test_009_Deposit_Money:
    baseURL = Readconfig.getApplictionURL()
    loginid = Readconfig.getUserId()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()

    def test_deposit_money(self,setup):
        self.logger.info("********** Test_009_Deposit_Money **********")


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
        self.logger.info("***************** Proving info to deposit Money  ********")
        self.depom=Deposit_Money(self.driver)
        self.depom.wait()
        self.depom.click_on_transaction_linked_text()
        self.depom.click_on_deposit_money_linked_text()

        self.depom.set_account_number("117501000811409")
        self.depom.set_amount(500)
        self.depom.deposit_type_drop_down("Cash")
        self.depom.set_perticulers("abcdefg")
        self.depom.click_on_submit()

        self.logger.info("******************** Save Deposit Money ************ ")
        self.msg = self.depom.deposit_money_alert()
        self.logger.info("************ Deposit Money Validation Started ************")

        if "Amount deposited successfully..." in self.msg:

            assert True == True
            self.logger.info("*********** Deposit Money Test Passed ************")
            print(self.driver.title)
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Deposit_Money.png")
            self.logger.error("******** Deposit Money Test Failed **********")
            assert True == False
            self.driver.quit()




