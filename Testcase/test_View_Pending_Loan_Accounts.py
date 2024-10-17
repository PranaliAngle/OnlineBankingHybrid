from PageObject.Loan import Loan
from PageObject.Loginpage import Loginpage
from Utilities.customLogger import LogGen
from Utilities.readProperties import Readconfig



class Test_007_View_Pending_loan_Accounts:
    baseURL = Readconfig.getApplictionURL()
    loginid = Readconfig.getUserId()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()

    def test_view_pending_loan_accounts(self, setup):
        self.logger.info("********** Test_007_View_Pending_loan_Accounts **********")
        self.logger.info("********** Starting login Page *******")

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
        self.logger.info("***************** Starting View Pending Loan Accounts ***************")
        self.loan=Loan(self.driver)
        self.loan.click_on_loan()
        self.loan.click_on_pending_loan_account_linked_text()
        self.logger.info("***************** View Pending Loan Accounts test case is passed ***************")