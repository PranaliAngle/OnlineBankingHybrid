

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

class Withdraw_Money:

    transaction_linked_text = "Transaction"
    withdraw_money_linked_text="Withdraw Money"
    account_no_by_name="account"

   #acc_no_textbox_by_name = '//*[@id="templatemo-preferences-form"]/div[1]/div[1]/input'
    amount_textbox_by_name = "amount"

    perticulers_by_name = "particulars"
    submit_btn_by_name = "submit"

    def __init__(self, driver):
        self.driver = driver

    def wait(self):
        self.driver.implicitly_wait(10)

    def click_on_transaction_linked_text(self):
        self.driver.find_element(By.LINK_TEXT, self.transaction_linked_text).click()

    def click_on_deposit_money_linked_text(self):
        self.driver.find_element(By.LINK_TEXT, self.withdraw_money_linked_text).click()

    def set_account_number(self,acc_no):
        element=self.driver.find_element(By.NAME,self.account_no_by_name)
        # Create action chain object
        action = ActionChains(self.driver)
        action.click_and_hold(on_element=element)
        action.send_keys(acc_no).release(on_element=element).perform()



    def set_amount(self, amt):
        self.driver.find_element(By.NAME, self.amount_textbox_by_name).send_keys(amt)


    def set_perticulers(self, perticulars):
        self.driver.find_element(By.NAME, self.perticulers_by_name).send_keys(perticulars)

    def click_on_submit(self):
        self.driver.find_element(By.NAME, self.submit_btn_by_name).click()

    def withdraw_money_alert(self):
        # create alert object
        alert = Alert(self.driver)
        self.msg = alert.text
        # get alert text
        print(self.msg)
        # accept the alert
        alert.accept()
        return self.msg