from telnetlib import EC

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Deposit_Money:

    transaction_linked_text="Transaction"
    deposit_money_linked_text="Deposit Money"
    acc_no_textbox_by_name='account'
    amount_textbox_by_name="amount"
    deposit_type_dropdown_by_name="deposittype"
    perticulers_by_name="particulars"
    submit_btn_by_name="submit"

    def __init__(self,driver):
        self.driver=driver

    def wait(self):
        self.driver.implicitly_wait(10)

    def click_on_transaction_linked_text(self):
        self.driver.find_element(By.LINK_TEXT,self.transaction_linked_text).click()

    def click_on_deposit_money_linked_text(self):
        self.driver.find_element(By.LINK_TEXT,self.deposit_money_linked_text).click()

    def set_account_number(self,acc_no):
        element=self.driver.find_element(By.NAME,self.acc_no_textbox_by_name)
        # Create action chain object
        action = ActionChains(self.driver)
        action.click_and_hold(on_element = element)
        action.send_keys(acc_no).perform()

    def set_amount(self,amt):
        self.driver.find_element(By.NAME,self.amount_textbox_by_name).send_keys(amt)

    def deposit_type_drop_down(self,acc_type):
        acc_status = self.driver.find_element(By.NAME,self.deposit_type_dropdown_by_name)
        Select_status = Select(acc_status)
        Select_status.select_by_value(acc_type)

    def set_perticulers(self,perticulars):
        self.driver.find_element(By.NAME,self.perticulers_by_name).send_keys(perticulars)

    def click_on_submit(self):
        self.driver.find_element(By.NAME,self.submit_btn_by_name).click()

    def deposit_money_alert(self):
        # create alert object
        alert = Alert(self.driver)
        self.msg = alert.text
        # get alert text
        print(self.msg)
        # accept the alert
        alert.accept()
        return self.msg