from selenium.webdriver.common.keys import Keys

from locators import locators


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        # my account page elements
        self.username_input = locators.MyAccounPage.user_name_input
        self.password_input = locators.MyAccounPage.password_input
        self.reg_email_input = locators.MyAccounPage.reg_email_input
        self.reg_password = locators.MyAccounPage.reg_password
        self.logout_link = locators.MyAccounPage.logout_link
        self.my_account_link = locators.MyAccounPage.my_account_link
        self.error_message = locators.MyAccounPage.error_msg

    def open_page_my_account(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def log_in(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.password_input).send_keys(Keys.ENTER)

    def create_account(self, email, password):
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.reg_password).send_keys(password)
        self.driver.find_element(*self.reg_password).send_keys(Keys.ENTER)

    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.logout_link).is_displayed()

    def get_error_meassage(self):
        return self.driver.find_element(*self.error_message).text