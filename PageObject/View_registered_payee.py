from selenium.webdriver.common.by import By


class View_registered_payee:

    customer_linked_text = "Customer"
    view_registered_payee_linked_list="View Registered Payee"
    search_textbox_xpath='//*[@id="example_filter"]/label/input'

    table_id = "example"
    table_row_xpath = '//*[@id="example"]/thead/tr'
    table_col_xpath = '//*[@id="example"]/thead/tr/th'

    def __init__(self, driver):
        self.driver = driver

    def click_On_customer(self):
        self.driver.find_element(By.LINK_TEXT, self.customer_linked_text).click()


    def click_On_View_registered_payee(self):
        self.driver.find_element(By.LINK_TEXT, self.view_registered_payee_linked_list).click()


    def set_searchBox(self, customerName):
        self.driver.find_element(By.XPATH, self.search_textbox_xpath).send_keys(customerName)


    def get_no_rows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_row_xpath))


    def get_table_columns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_col_xpath))


    def search_customer_by_name(self, customer_name):
        flag = False
        for r in range(1, self.get_no_rows() + 1):
            table = self.driver.find_element(By.ID, self.table_id)
            name = table.find_element(By.XPATH, '//*[@id="example"]/tbody/tr/td[1]').text
            print(name)
            print(customer_name)
            if name == customer_name:
                flag = True
                break
        return flag


    def click_on_active(self):


        for r in range(1,self.get_no_rows()+1):
            self.driver.find_element(By.ID, self.table_id)
            self.driver.find_element(By.XPATH,'//*[@id="example"]/tbody/tr/td[9]/a[1]').click()
            print("to do active")


    def click_on_deactive(self):


        for r in range(1,self.get_no_rows()+1):
            self.driver.find_element(By.ID, self.table_id)
            self.driver.find_element(By.XPATH,'//*[@id="example"]/tbody/tr/td[9]/a[2]').click()


    def check_status(self):
        for r in range(1,self.get_no_rows()+1):
            table=self.driver.find_element(By.ID,self.table_id)
            stat_name=table.find_element(By.XPATH,'//*[@id="example"]/tbody/tr/td[8]').text
            return stat_name



