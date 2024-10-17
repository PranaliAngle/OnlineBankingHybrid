import time
import pytest
from selenium import webdriver
from PageObject.Loginpage import Loginpage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen


class Test_001_Login_Staff_Panel:

    #baseURL="https://banking.perfectinitsolutions.com/"
    #loginid="birbal"
    #password="birbalbirbal"

    baseURL=Readconfig.getApplictionURL()
    loginid=Readconfig.getUserId()
    password=Readconfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.Sanity
    def test_LoginPageTitle(self,setup):
        self.logger.info("********** Test_001_Login_title **********")
        self.logger.info("********** Verifying_Staff_Login_Page_Title **********")

       # self.driver=webdriver.chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.clickOnStaffLoginLink()
        act_title=self.driver.title


        if act_title=="Online Banking - Online Money Bank":
            self.logger.info("******** Staff Login Page Title is Passed *********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_StaffLoginPageTitle.png")
            self.logger.error("******** Staff Login Page Title is Failed *********")
            assert False

    @pytest.mark.Sanity
    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying_Login_Page **********")

        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=Loginpage(self.driver)
        self.lp.clickOnStaffLoginLink()
        self.lp.setLoginId(self.loginid)
        self.lp.setPassword(self.password)
        self.lp.clickSignIn()
        #print(self.driver.title)
        time.sleep(10)
        act_title=self.driver.title
        #self.driver.close()

        if act_title=="Online Banking - Online Money Bank":
            assert True
            self.logger.info("******** Staff Login Page is Passed *********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_StaffDashbordPageTitle.png")
            self.logger.error("******** Staff Login Page is Failed ********")
            assert False
