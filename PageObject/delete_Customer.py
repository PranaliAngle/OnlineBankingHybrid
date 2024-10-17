from selenium.webdriver.common.by import By

class Delete_Customer:

    table_id = "example"
    table_row_xpath = '//*[@id="example"]/thead/tr'
    table_col_xpath = '//*[@id="example"]/thead/tr/th'

    def __init__(self, driver):
        self.driver = driver

    def get_no_rows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_row_xpath))

    def get_table_columns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_col_xpath))

    def delete_customer(self):
        for r in range(1, self.get_no_rows() + 1):
            table = self.driver.find_element(By.ID, self.table_id)
            delete_column = table.find_element(By.XPATH, '//*[@id="example"]/tbody/tr[1]/td[7]/center/a[2]').click()
