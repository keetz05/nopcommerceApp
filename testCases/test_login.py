import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import CustomLogger
import random
import string



class Test_login_001:

    base_url = ReadConfig.get_application_url()
    user_email = ReadConfig.get_username()
    user_password = ReadConfig.get_password()
    log = CustomLogger.loggen()

    def test_homepage_title(self,setup):
        self.log.info("********** start home page testcase **********")
        self.log.info("********** verify login title same or not *********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(3)
        act_title = self.driver.title
        if act_title == "Your Store":
            self.log.info("********** title of the login page sucessfull **********")
            print("Login Successfully")
            assert True
            self.driver.close()

        else:
            self.log.info("********** title of the login page failed**********")
            print("Login Failed")
            self.driver.close()
            assert False

    def test_login_validation(self,setup):
        self.log.info("********** start login validation **********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(3)
        self.login = LoginPage(self.driver)
        self.log.info("********** login validation start **********")
        self.login.set_myaccount()
        self.login.set_login()
        act_title1 = self.driver.title
        if act_title1 == "Account Login":
            self.log.info("********** title of the login page sucessfully **********")
            assert True
        else:
            assert False
        time.sleep(3)
        self.email = random_generator() + "@gmail.com"
        self.login.setUserEmail(self.email)
        self.login.setPassword(self.user_password)
        self.login.set_btn_login()
        act_title = self.driver.title
        if act_title == "My Account":
            self.log.info("********** test passed   **********")
            assert True
        else:
            self.log.info("********** test failed **********")
            assert False
        self.login.set_myaccount()
        self.login.set_link_logout()
        self.login.set_btn_continue()
        self.log.info("********** login validation end test passed    **********")
        self.driver.close()

def random_generator(size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))






