'Fund Transferred successfully..'
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Fund_Transfer:
    transaction_linked_text = "Transaction"

    fund_transfer_linked_text="Fund Transfer"
    account_no_by_name="account"
    registered_payee_ddl="regpayeeid"
    amount_txtbox_by_name="amount"
    perticulars_txtbox_by_name='particulars'
    submit_btn_by_name='submit'

    def __init__(self,driver):
        self.driver=driver

    def wait(self):
        self.driver.implicitly_wait(10)
    def click_on_transaction_linked_text(self):
        self.driver.find_element(By.LINK_TEXT, self.transaction_linked_text).click()

    def click_on_fund_transfer(self):
        self.driver.execute_script("window.scrollBy(0, 500)")
        self.driver.find_element(By.LINK_TEXT,self.fund_transfer_linked_text).click()

    def set_account_no(self,acc_no):
        element=self.driver.find_element(By.NAME,self.account_no_by_name)
        action=ActionChains(self.driver)
        action.click_and_hold(on_element=element)
        action.send_keys(acc_no).perform()


    def select_registerd_payee_ddl(self,reg_payee):
        element=self.driver.find_element(By.NAME,self.registered_payee_ddl)
        select=Select(element)
        select.select_by_value(reg_payee)

    def set_amount(self,amt):
        self.driver.find_element(By.NAME,self.amount_txtbox_by_name).send_keys(amt)

    def set_perticulars(self,per):
        self.driver.find_element(By.NAME,self.perticulars_txtbox_by_name).send_keys(per)


    def click_on_submit_btn(self):
        self.driver.find_element(By.NAME,self.submit_btn_by_name).click()


    def fund_transfer_alert(self):
        # create alert object
        alert = Alert(self.driver)
        self.msg = alert.text
        # get alert text
        print(self.msg)
        # accept the alert
        alert.accept()
        return self.msg