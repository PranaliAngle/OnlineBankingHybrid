from selenium.webdriver.common.by import By


class View_Loan_Account:

    view_loan_accounts_linked_text="View Loan Accounts"
    search_textBox_xpath='//*[@id="example_filter"]/label/input'

    table_id = "example"
    table_row_xpath = '//*[@id="example"]/thead/tr'
    table_col_xpath = '//*[@id="example"]/thead/tr/th'

    header="//*[@class='templatemo-content']/h1"

    def __init__(self, driver):
        self.driver = driver

    def get_no_rows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_row_xpath))

    def get_table_columns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_col_xpath))

    def click_On_view_acounts(self):
        self.driver.find_element(By.LINK_TEXT, self.view_loan_accounts_linked_text).click()

    def set_searchBox(self,customerName):
        self.driver.find_element(By.XPATH,self.search_textBox_xpath).send_keys(customerName)

    def search_customer_by_name(self,customer_name):
        flag=False
        for r in range(1,self.get_no_rows()+1):
            table=self.driver.find_element(By.ID,self.table_id)
            name=table.find_element(By.XPATH,'//*[@id="example"]/tbody/tr/td[1]').text
            print(name)
            print(customer_name)
            if name==customer_name:
                flag=True
                break
        return flag

    def click_on_View(self):
        self.driver.find_element(By.XPATH, '//*[@id="example"]/tbody/tr/td[11]/a').click()


    def get_header(self):
        return self.driver.find_element(By.XPATH,self.header).text
