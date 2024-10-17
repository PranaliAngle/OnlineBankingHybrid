
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Make_Loan_Payment:

    transaction_linked_text = "Transaction"
    make_loan_payment_linked_text="Make Loan Payment"
    account_no_by_name="loanaccountno"
    payment_type_dropdown_by_name = "paymenttype"

   #acc_no_textbox_by_name = '//*[@id="templatemo-preferences-form"]/div[1]/div[1]/input'
    amount_textbox_by_id = "paidamt"

    perticulers_by_name = "particulars"
    submit_btn_by_name = "submit"

    def __init__(self, driver):
        self.driver = driver

    def wait(self):
        self.driver.implicitly_wait(10)

    def click_on_transaction_linked_text(self):
        self.driver.find_element(By.LINK_TEXT, self.transaction_linked_text).click()

    def click_on_make_loan_payment(self):
        self.driver.find_element(By.LINK_TEXT, self.make_loan_payment_linked_text).click()

    def set_account_number(self, acc_no):
        element=self.driver.find_element(By.NAME, self.account_no_by_name)
        # Create action chain object
        action = ActionChains(self.driver)

        # Click on the item
        action.click(on_element=element)

        action.send_keys(acc_no)
        #action.__enter__()
        action.release(on_element=element)
        # Perform the operation
        action.perform()


    def set_amount(self, amt):
        self.driver.find_element(By.ID, self.amount_textbox_by_id).send_keys(amt)

    def payment_type_drop_down(self, acc_type):
        acc_status = self.driver.find_element(By.NAME,self.payment_type_dropdown_by_name)
        Select_status = Select(acc_status)
        Select_status.select_by_value(acc_type)

    def click_on_submit(self):
        self.driver.find_element(By.NAME, self.submit_btn_by_name).click()

    def make_loan_payment_alert(self):
        # create alert object
        alert = Alert(self.driver)
        self.msg = alert.text
        # get alert text
        print(self.msg)
        # accept the alert
        alert.accept()
        return self.msg