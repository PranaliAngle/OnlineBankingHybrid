import os
from selenium import webdriver

# Retrieve the path from environment variable
driver_path = os.getenv('CHROMEDRIVER_PATH')

driver = webdriver.Chrome(executable_path=driver_path)