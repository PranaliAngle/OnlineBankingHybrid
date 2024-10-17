

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Add_Registered_Payee:

    transaction_linked_text = "Transaction"
    add_registered_payee_linked_text="Add Registered Payee"
    account_no_txtbox_by_name='acno'
    fund_transfer_type_by_name='trtype'
    bank_account_no_txtbox_by_name='bankacno'
    submit_btn='submit'

    payee_name_textbox_name="payeename"
    account_type_ddl='accounttype'
    bank_name_txtbox_name='bankname'
    ifsccode_by_name='ifsccode'

    def __init__(self,driver):
        self.driver=driver

    def wait(self):
        self.driver.implicitly_wait(10)

    def click_on_transaction_linked_text(self):
        self.driver.find_element(By.LINK_TEXT, self.transaction_linked_text).click()

    def click_on_add_registered_payee(self):
        self.driver.execute_script("window.scrollBy(0, 500)")
        self.driver.find_element(By.LINK_TEXT,self.add_registered_payee_linked_text).click()



    def set_account_no(self,acc_no):
        self.driver.find_element(By.NAME,self.account_no_txtbox_by_name).send_keys(acc_no)
        #action=ActionChains(ele)
        #action.click_and_hold(on_element=ele).send_keys(acc_no).perform()

    def select_fund_transfer_type_ddl(self,value):
        ele=self.driver.find_element(By.NAME,self.fund_transfer_type_by_name)
        select_type=Select(ele)
        select_type.select_by_value(value)

    def set_bank_account_no(self,acc_no):
        self.driver.find_element(By.NAME,self.bank_account_no_txtbox_by_name).send_keys(acc_no)
        #action = ActionChains(ele)
        #action.click_and_hold(on_element=ele).send_keys(acc_no).release(on_element=ele).perform()

    def click_on_submit(self):
        self.driver.find_element(By.NAME,self.submit_btn).click()

    def add_registered_payee_alert(self):
        # create alert object
        alert = Alert(self.driver)
        self.msg = alert.text
        # get alert text
        print(self.msg)
        # accept the alert
        alert.accept()
        return self.msg


    def set_payeename(self,name):
        self.driver.find_element(By.NAME,self.payee_name_textbox_name).send_keys(name)

    def select_acc_Type(self,acc_type):
        ele=self.driver.find_element(By.NAME,self.account_type_ddl)
        select_type=Select(ele)
        select_type.select_by_value(acc_type)


    def set_bank_name(self,bankname):
        self.driver.find_element(By.NAME,self.bank_name_txtbox_name).send_keys(bankname)

    def set_ifsccode(self,ifsccode):
        self.driver.find_element(By.NAME,self.ifsccode_by_name).send_keys(ifsccode)


        

