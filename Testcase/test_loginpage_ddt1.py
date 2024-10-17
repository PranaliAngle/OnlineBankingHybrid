import time
import pytest
from selenium import webdriver
from PageObject.Loginpage import Loginpage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen
from Utilities import ExcelUtils

class Test_001_Login_Staff_Panel:

    baseURL="https://banking.perfectinitsolutions.com/"
    path=".//TestData/TestData.xlsx"
    #loginid="birbal"
    #password="birbalbirbal"



    logger=LogGen.loggen()



    def test_login_ddt(self,setup):
        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows i a Excel:", self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.logger.info("********** Test_001_ddt_Login **********")
            self.logger.info("********** Verifying_Login_Page **********")
            print("Rows:",r)
            self.driver=setup
            self.driver.implicitly_wait(10)
            self.driver.set_page_load_timeout(30)  # Increase page load timeout

            self.driver.get(self.baseURL)

            self.lp=Loginpage(self.driver)



            self.loginId=ExcelUtils.readData(self.path,'Sheet1',r,1)
            self.password=ExcelUtils.readData(self.path,'Sheet1',r,2)
            self.exp=ExcelUtils.readData(self.path,'Sheet1',r,3)

            self.lp.clickOnStaffLoginLink()
            self.lp.setLoginId(self.loginId)
            self.lp.setPassword(self.password)
            self.lp.clickSignIn()
            #time.sleep(5)

            act_title=self.driver.title
            exp_title="Online Banking - Online Money Bank"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("********Passed************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("*******Failed***********")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("********failed***********")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("*********Passed************")
                    lst_status.append("Pass")

            if "Fail" not in lst_status:
                 self.logger.info("login DDT test Passed.......")
                 self.driver.quit()
                 #time.sleep(10)
                 assert True
            else:
                 self.logger.info("login DDT test Failed.......")
                 self.driver.quit()
                 #time.sleep(10)
                 assert False


        self.logger.info("********** End of Login DDT Test***********")
        self.logger.info("************completed TC_LoginDDT_002***************")