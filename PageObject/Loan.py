from selenium.webdriver.common.by import By


class Loan:
    loan_linked_text="Loan"
    pending_loan_account_linked_text="Pending Loan Accounts"

    def __init__(self,driver):
        self.driver=driver

    def click_on_loan(self):
        self.driver.find_element(By.LINK_TEXT,self.loan_linked_text).click()

    def click_on_pending_loan_account_linked_text(self):
        self.driver.find_element(By.LINK_TEXT,self.pending_loan_account_linked_text).click()