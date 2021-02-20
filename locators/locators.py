from selenium.webdriver.common.by import By


class BillingAddressLoactors:

    reg_email = (By.ID, "reg_email")
    reg_password = (By.ID, "reg_password")
    reg_address = (By.LINK_TEXT, "Addresses")
    reg_edit = (By.LINK_TEXT, "Edit")
    billing_first_name = (By.ID, "billing_first_name")
    billing_last_name = (By.ID, "billing_last_name")
    billing_company_name = (By.ID, "billing_company")
    billing_country = (By.ID, "billing_country")
    billing_address_street = (By.ID, "billing_address_1")
    billing_postcode = (By.ID, "billing_postcode")
    billing_city = (By.ID, "billing_city")
    billing_phone = (By.ID, "billing_phone")
    save_button = (By.XPATH, "//button[@value='Save address']")
    messages = (By.CLASS_NAME, "woocommerce-message")


class MyAccounPage:

    my_account_link = (By.XPATH, "//li[@id='menu-item-22']//a")
    user_name_input = (By.ID, "username")
    password_input = (By.ID, "password")
    reg_email_input = (By.ID, "reg_email")
    reg_password = (By.ID, "reg_password")
    button_login = (By.NAME, "login")
    logout_link = (By.LINK_TEXT, "Logout")
    error_msg = (By.XPATH, "//ul[@class='woocommerce-error']//li")


