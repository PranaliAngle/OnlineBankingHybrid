import pytest

from PageObject.Loginpage import Loginpage
from PageObject.Fund_Transfer import Fund_Transfer
from Utilities.customLogger import LogGen
from Utilities.readProperties import Readconfig

class Test_012_Fund_Transfer:
    baseURL = Readconfig.getApplictionURL()
    loginid = Readconfig.getUserId()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_fund_transfer(self,setup):
        self.logger.info("********** Test_012_Fund_Transfer **********")


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
        self.logger.info("***************** Proving info Fund transfer  ********")
        self.ftrans=Fund_Transfer(self.driver)
        self.ftrans.wait()
        self.ftrans.click_on_transaction_linked_text()
        self.ftrans.click_on_fund_transfer()
        self.ftrans.set_account_no("117501000811409")
        self.ftrans.select_registerd_payee_ddl("14")
        self.ftrans.set_amount("300")
        self.ftrans.set_perticulars("abcdefg")
        self.ftrans.click_on_submit_btn()
        self.ftrans.wait()
        self.logger.info("******************** Save Fund Transfer ************ ")
        self.msg = self.ftrans.fund_transfer_alert()
        self.logger.info("****** Fund Transfer Validation Started ************")
        self.msg1="Fund Transferred successfully.."
        if self.msg1==self.msg:

            assert True == True
            self.logger.info("*********** Fund Transfer Test Passed ************")
            print(self.driver.title)
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_fund_transfer.png")
            self.logger.error("******** Fund Transfer Test Failed **********")
            assert True == False
            self.driver.quit()
