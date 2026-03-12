from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Register:
    link_my_account_XPATH = '//a[@title="My Account"]'
    link_Register_XPATH = '//a[text()="Register"]'
    textbox_first_name_XPATH = '//input[@id="input-firstname"]'
    textbox_last_name_XPATH = '//input[@id="input-lastname"]'
    textbox_email_XPATH = '//input[@id="input-email"]'
    textbox_telephone_XPATH = '//input[@id="input-telephone"]'
    textbox_password_XPATH = '//input[@id="input-password"]'
    textbox_confirmation_XPATH = '//input[@id="input-confirm"]'
    radio_options_btn_XPATH = '//*[@id="content"]/form/fieldset[3]/div/div/label[1]/input'
    check_box_privacy_policy_XPATH = '//*[@id="content"]/form/div/div/input[1]'
    btn_continue_XPATH = '//input[@type="submit"]'
    btn_access_XPATH = '//a[text()="Continue"]'

    def __init__(self,driver):
        self.driver = driver

    def set_my_account(self):
        wait = WebDriverWait(self.driver, 10)
        my_account_field = wait.until(EC.presence_of_element_located((By.XPATH, self.link_my_account_XPATH)))
        my_account_field.click()

    def set_register(self):
        wait = WebDriverWait(self.driver, 10)
        my_account_field = wait.until(EC.presence_of_element_located((By.XPATH, self.link_Register_XPATH)))
        my_account_field.click()

    def set_first_name(self,first_name):
        wait = WebDriverWait(self.driver, 10)
        first_name_field = wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_first_name_XPATH)))
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def set_last_name(self,last_name):
        wait = WebDriverWait(self.driver, 10)
        last_name_field = wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_last_name_XPATH)))
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def set_email(self,email):
        wait = WebDriverWait(self.driver, 10)
        email_field = wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_email_XPATH)))
        email_field.clear()
        email_field.send_keys(email)

    def set_telephone(self,telephone):
        wait = WebDriverWait(self.driver, 10)
        phonenumber_field = wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_telephone_XPATH)))
        phonenumber_field.clear()
        phonenumber_field.send_keys(telephone)

    def set_password(self,password):
        wait = WebDriverWait(self.driver, 10)
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_password_XPATH)))
        password_field.clear()
        password_field.send_keys(password)

    def set_confirmation(self,confirmation):
        wait = WebDriverWait(self.driver, 10)
        confirmation_field = wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_confirmation_XPATH)))
        confirmation_field.clear()
        confirmation_field.send_keys(confirmation)

    def set_radio_btn(self):
        wait = WebDriverWait(self.driver, 10)
        radio_btn_fields = wait.until(EC.presence_of_element_located((By.XPATH,self.radio_options_btn_XPATH)))
        radio_btn_fields.click()

    def set_privacypolicy(self):
        wait = WebDriverWait(self.driver, 10)
        privacy_policy_fields = wait.until(EC.presence_of_element_located((By.XPATH, self.check_box_privacy_policy_XPATH)))
        privacy_policy_fields.click()

    def set_btn_continue(self):
        wait = WebDriverWait(self.driver, 10)
        continue_field = wait.until(EC.presence_of_element_located((By.XPATH, self.btn_continue_XPATH)))
        continue_field.click()

    def set_btn_access(self):
        wait = WebDriverWait(self.driver, 10)
        access_field = wait.until(EC.presence_of_element_located((By.XPATH, self.btn_access_XPATH)))
        access_field.click()

