import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_update_billing_address():
    email = str(random.randint(0,1000))+ "maciek@maciek.com"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("MaciekMacie")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//li")
    driver.find_element(By.LINK_TEXT, "Addresses").click()
    driver.find_element(By.LINK_TEXT, "Edit").click()
    driver.find_element(By.ID, "billing_first_name").send_keys("Maciek")
    driver.find_element(By.ID, "billing_last_name").send_keys("Sikora")
    driver.find_element(By.ID, "billing_company").send_keys("Dzonny")
    Select(driver.find_element(By.ID, "billing_country")).select_by_visible_text("Poland")
    driver.find_element(By.ID, "billing_address_1").send_keys("Ulica 1")
    driver.find_element(By.ID, "billing_postcode").send_keys("33-000")
    driver.find_element(By.ID, "billing_city").send_keys("Kraków")
    driver.find_element(By.ID, "billing_phone").send_keys("070072772")
    driver.find_element(By.XPATH, "//button[@value='Save address']").click()
    assert "Address changed successfully" in driver.find_element((By.CLASS_NAME, "woocommerce-message")).text

    #assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()