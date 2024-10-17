import time

from PageObject.Loginpage import Loginpage
from PageObject.Make_Loan_Payment import Make_Loan_Payment
from Utilities.customLogger import LogGen
from Utilities.readProperties import Readconfig

class Test_011_Make_Loan_Payment:
    baseURL = Readconfig.getApplictionURL()
    loginid = Readconfig.getUserId()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()

    def test_make_loan_payment(self,setup):
        self.logger.info("********** Test_011_Make_loan_Payment **********")


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
        self.logger.info("***************** Proving info to Make Loan Payment  ********")
        self.mlpay=Make_Loan_Payment(self.driver)
        self.mlpay.wait()
        self.mlpay.click_on_transaction_linked_text()
        self.mlpay.click_on_make_loan_payment()
        self.mlpay.set_account_number("117501000811409")

        #self.depom.set_acc_no("117501000811409")
        self.mlpay.set_amount(10)
        self.mlpay.payment_type_drop_down("Cash")

        self.mlpay.click_on_submit()
        self.mlpay.wait()
        self.logger.info("******************** Save Loan Payment ************ ")
        self.msg = self.mlpay.make_loan_payment_alert()
        self.logger.info("************ Make Loan Payment Validation Started ************")

        if "Loan payment record inserted successfully.." in self.msg:

            assert True == True
            self.logger.info("*********** Make Loan Payment Test Passed ************")
            print(self.driver.title)
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_make_loan_payment.png")
            self.logger.error("******** Make loan payment Test Failed **********")
            assert True == False
            self.driver.quit()
