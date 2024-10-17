from selenium.webdriver.common.by import By

class Loginpage:

    staff_login_linked_text="Staff Login Panel"
    textbox_login_id="username"
    textbox_password_id="password"
    btn_signin_id="submit"
    logout_linked_text="Logout"

    def __init__(self,driver):
        self.driver=driver



    def clickOnStaffLoginLink(self):
        self.driver.find_element(By.LINK_TEXT,self.staff_login_linked_text).click()


    def setLoginId(self,loginid):
        self.driver.find_element(By.ID,self.textbox_login_id).send_keys(loginid)
        #self.driver.find_element(By.LINK_TEXT,self.staff_login_linked_text).send_keys()

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickSignIn(self):
        self.driver.find_element(By.ID,self.btn_signin_id).click()


    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.logout_linked_text).click()


