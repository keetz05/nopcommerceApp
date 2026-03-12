import string
import time
from selenium import webdriver
# from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from pageObjects.Register import Register
from utilities.customLogger import CustomLogger
import random

class TestRegiter_001():
    base_url = ReadConfig.get_application_url()
    firstname = ReadConfig.get_first_name()
    lastname = ReadConfig.get_last_name()
    Email = ReadConfig.get_email()
    telephone = ReadConfig.get_phone()
    password =ReadConfig.get_Password_fields()
    confirm_password =ReadConfig.get_confirm_password()
    log = CustomLogger.loggen()


    def test_regsiter(self,setup):
        self.driver = setup
        self.log.info("********* successfully open applications  **********")
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.reg = Register(self.driver)
        self.reg.set_my_account()
        self.reg.set_register()
        self.log.info("********* successfully entered regsister page  **********")
        act_title = self.driver.title
        if act_title == "Register Account":
            self.log.info("**********successfully captured login title ***********")
            assert True
        else:
            self.log.info("********* failed ***********")
            assert False

        self.reg.set_first_name(self.firstname)
        self.reg.set_last_name(self.lastname)
        self.email = random_generator() + "@gmail.com"
        self.reg.set_email(self.email)
        self.reg.set_telephone(self.telephone)
        self.reg.set_password(self.password)
        self.reg.set_confirmation(self.confirm_password)
        self.reg.set_radio_btn()
        self.reg.set_privacypolicy()
        self.reg.set_btn_continue()
        self.reg.set_btn_access()
        self.log.info("********* successfully captured regsiter page  testcase passed **********")
        self.driver.close()




def random_generator(size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))




