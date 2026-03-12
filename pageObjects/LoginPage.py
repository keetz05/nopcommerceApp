from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    link_my_account_XPATH = '//a[@title="My Account"]'
    link_login_XPATH = '//a[text()="Login"]'
    textbox_email_XPATH = '//input[@id="input-email"]'
    textbox_password_XPATH = '//input[@id="input-password"]'
    btn_login_XPATH = '//input[@type="submit"]'
    link_logout_XPATH = '//a[text()="Logout"]'
    btn_continue_XPATH = '//a[text()="Continue"]'


    def __init__(self,driver):
        self.driver = driver

    def set_myaccount(self):
        wait = WebDriverWait(self.driver, 10)
        my_account_fields = wait.until(EC.presence_of_element_located((By.XPATH,self.link_my_account_XPATH)))
        my_account_fields.click()

    def set_login(self):
        wait = WebDriverWait(self.driver, 10)
        login_fields = wait.until(EC.presence_of_element_located((By.XPATH,self.link_login_XPATH)))
        login_fields.click()

    def setUserEmail(self,user_email):
        wait = WebDriverWait(self.driver, 10)
        user_fields = wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_email_XPATH)))
        user_fields.clear()
        user_fields.send_keys(user_email)

    def setPassword(self,user_password):
        wait = WebDriverWait(self.driver, 10)
        password_fields = wait.until(EC.presence_of_element_located((By.XPATH,self.textbox_password_XPATH)))
        password_fields.clear()
        password_fields.send_keys(user_password)

    def set_btn_login(self):
        wait = WebDriverWait(self.driver, 10)
        login_fields = wait.until(EC.presence_of_element_located((By.XPATH,self.btn_login_XPATH)))
        login_fields.click()

    def set_link_logout(self):
        wait = WebDriverWait(self.driver, 10)
        logout_fields = wait.until(EC.presence_of_element_located((By.XPATH,self.link_logout_XPATH)))
        logout_fields.click()

    def set_btn_continue(self):
        wait = WebDriverWait(self.driver, 10)
        btn_continue_fields = wait.until(EC.presence_of_element_located((By.XPATH,self.btn_continue_XPATH)))
        btn_continue_fields.click()




