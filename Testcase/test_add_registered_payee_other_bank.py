import time

from PageObject.Loginpage import Loginpage
from PageObject.Add_Registered_Payee import Add_Registered_Payee
from Utilities.customLogger import LogGen
from Utilities.readProperties import Readconfig

class Test_014_Add_registered_payee_other_bank:

    baseURL = Readconfig.getApplictionURL()
    loginid = Readconfig.getUserId()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()

    def test_add_registered_payee_other_bank(self,setup):
        self.logger.info("********** Test_014_Add_Registered_Payee_other_bank **********")


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
        self.logger.info("***************** Proving info to add registered payee other bank  ********")
        self.addrpay=Add_Registered_Payee(self.driver)
        self.addrpay.wait()
        self.addrpay.click_on_transaction_linked_text()
        self.addrpay.click_on_add_registered_payee()
        self.addrpay.set_account_no("117501000811409")
        self.addrpay.select_fund_transfer_type_ddl("Other bank")
        self.addrpay.set_payeename("Pranali")
        self.addrpay.set_bank_account_no("117501000812401")
        self.addrpay.select_acc_Type("Savings")
        self.addrpay.set_bank_name("SBI")
        self.addrpay.set_ifsccode("SBI-BHOSARI")
        self.addrpay.click_on_submit()
        time.sleep(5)
        self.logger.info("******************** Save registered payee ************ ")
        self.msg = self.addrpay.add_registered_payee_alert()
        self.logger.info("****** Registered payee Validation Started ************")
        self.msg1="Registered payee record inserted successfully.."

        if self.msg1==self.msg:

            assert True == True
            self.logger.info("*********** Add Registered payee other bank Test Passed ************")
            print(self.driver.title)
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_registered_payee_other_bank.png")
            self.logger.error("******** Add registered payee other bank Test Failed **********")
            assert True == False
            self.driver.quit()
