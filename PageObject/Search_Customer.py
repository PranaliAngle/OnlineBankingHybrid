from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Search_Customer:
    customer_linked_text = "Customer"
    view_customer_linked_text="View Customer"
    search_box_xpath='//*[@id="example_filter"]/label/input'
    view_xpath='//*[@id="example"]/tbody/tr[1]/td[8]/a'
    table_id="example"
    table_row_xpath='//*[@id="example"]/thead/tr'
    table_col_xpath='//*[@id="example"]/thead/tr/th'

    def __init__(self, driver):
        self.driver = driver

    def click_On_customer(self):
        self.driver.find_element(By.LINK_TEXT, self.customer_linked_text).click()

    def click_On_View_customer(self):
        self.driver.find_element(By.LINK_TEXT,self.view_customer_linked_text).click()

    def set_searchBox(self,customerName):
        self.driver.find_element(By.XPATH,self.search_box_xpath).send_keys(customerName)



    def get_no_rows(self):
        return len(self.driver.find_elements(By.XPATH,self.table_row_xpath))


    def get_table_columns(self):
        return len(self.driver.find_elements(By.XPATH,self.table_col_xpath))


    def search_customer_by_name(self,customer_name):
        flag=False
        for r in range(1,self.get_no_rows()+1):
            table=self.driver.find_element(By.ID,self.table_id)
            name=table.find_element(By.XPATH,'//*[@id="example"]/tbody/tr/td[3]').text
            print(name)
            print(customer_name)
            if name==customer_name:
                flag=True
                break
        return flag






    def click_on_view(self):
        self.driver.find_element(By.LINK_TEXT,self.view_xpath).click()
