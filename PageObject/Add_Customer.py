from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Customer:

    customer_linked_text="Customer"
    Add_customer_linked_text="Add Customer"
    Firstname_textbox_by_name="firstname"
    Lastname_textbox_by_name="lastname"
    loginid_textbox_by_name="loginid"
    account_login_password_by_name="accountpassword"
    confirm_login_password_by_name="confirmloginpassword"
    #confirm_login_password_by_name='//*[@id="templatemo-preferences-form"]/div[6]/div[1]/input'
    transaction_password_textbox_by_name="transactionpassword"
    confirm_transaction_password_textbox_by_name="confirmtransactionpassword"
    mobile_no_textbox_by_name="mob_no"
    emailid_textbox_by_name="emailid"
    address_textbox_by_name="address"
    city_textbox_by_name="city"
    state_dropdownlist_by_name='State'
    account_status_dropdown_by_name="accountstatus"
    submit_btn_by_name="submit"

    def __init__(self,driver):
        self.driver=driver

    def click_On_customer(self):
        self.driver.find_element(By.LINK_TEXT,self.customer_linked_text).click()

    def click_On_Add_Customer(self):
        self.driver.find_element(By.LINK_TEXT,self.Add_customer_linked_text).click()

    def set_customer_firstname(self,firstname):
        self.driver.find_element(By.NAME,self.Firstname_textbox_by_name).send_keys(firstname)

    def set_customer_lastname(self,lastname):
        self.driver.find_element(By.NAME,self.Lastname_textbox_by_name).send_keys(lastname)

    def set_customer_loginid(self,loginid):
        self.driver.find_element(By.NAME,self.loginid_textbox_by_name).send_keys(loginid)

    def set_account_password(self,accountpassword):
        self.driver.find_element(By.NAME,self.account_login_password_by_name).send_keys(accountpassword)

    def set_confirm_login_password(self,confirm_accountpassword):
        self.driver.find_element(By.NAME,self.confirm_login_password_by_name).send_keys(confirm_accountpassword)
       # element = WebDriverWait(self.driver, 10).until(
            #EC.presence_of_element_located((By.ID, self.s))
    def set_transaction_password(self,transaction_password):
        self.driver.find_element(By.NAME,self.transaction_password_textbox_by_name).send_keys(transaction_password)

    def set_confirm_transaction_password(self,confirm_transaction_password):
        self.driver.find_element(By.NAME,self.confirm_transaction_password_textbox_by_name).send_keys(confirm_transaction_password)


    def set_mobile_no(self,mobile_no):
        self.driver.find_element(By.NAME,self.mobile_no_textbox_by_name).send_keys(mobile_no)

    def set_emailid(self,emailid):
        self.driver.find_element(By.NAME,self.emailid_textbox_by_name).send_keys(emailid)

    def set_adderss(self,adder):
        self.driver.find_element(By.NAME,self.address_textbox_by_name).send_keys(adder)

    def set_city(self,city):
        self.driver.find_element(By.NAME,self.city_textbox_by_name).send_keys(city)

    def set_state(self,state_value):
        state=self.driver.find_element(By.NAME,self.state_dropdownlist_by_name)
        select_state=Select(state)
        select_state.select_by_value(state_value)

    def set_account_status(self,status_value):
        acc_status=self.driver.find_element(By.NAME,self.account_status_dropdown_by_name)
        Select_status=Select(acc_status)
        Select_status.select_by_value(status_value)

    def click_on_submit(self):
        self.driver.find_element(By.NAME,self.submit_btn_by_name).click()




