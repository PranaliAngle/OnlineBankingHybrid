from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service


@pytest.fixture()
def setup(browser):
    #chrome_service = Service(executable_path=r'C:\Users\Dell\PycharmProjects\OnlineBanking\Driver\chromedriver-win64\chromedriver.exe')
    #chrome_options = Options()
    #chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    #chrome_options.add_argument("--verbose")
    #service = Service(executable_path='.\\Driver\\chromedriver-win64\\chromedriver.exe')
    #driver=webdriver.Chrome(options=chrome_options)
    chrome_options = webdriver.ChromeOptions()

    #driver = webdriver.Chrome(options=options)

    if browser == 'Chrome':
        driver = webdriver.Chrome(options=chrome_options)
        print("Launching Chrome Browser..........")

    elif browser == 'Firefox':
        driver=webdriver.Firefox(options=chrome_options)
        print("Launching FireFox Browser............")

    else:
        driver = webdriver.Ie()

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
 config._metadata = {
    "Project Name": "Hybrid Framework Practice",
    "Module Name": "Customers",
    "Tester":"Pranali"
 }

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)



