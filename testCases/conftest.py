from selenium import webdriver
import pytest

@pytest.fixture()

def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("********************started chrome browser ********************")

    elif browser == "edge":
        driver = webdriver.Edge()
        print("********************started Edge  browser ********************")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("********************started firefox browser *********************")

    else:
        driver = webdriver.Chrome()
        print ("**** default chrome browser started **********")

    return driver
#terminal request using this method
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser (request):
    return request.config.getoption("--browser")

#----------------pytest html report --------------

def pytest_configure (config):
    if hasattr(config,"metadata"):
        config._metadata['Project name '] ='nopcommerceProject'
        config._metadata['Module name '] ='Login page'
        config._metadata['Tester name '] ='Keerthana'

#it is hook for delete /modify environment info to html report

def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)