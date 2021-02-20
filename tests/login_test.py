from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.my_account_page import MyAccountPage
import pytest

# maciek@maciek.com
# MaciekMacie
# monika@monika.com
# MonikaMonik

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page_my_account()
        my_account_page.log_in("maciek@maciek.com", "MaciekMacie")

        assert my_account_page.is_logout_link_displayed()

    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page_my_account()
        my_account_page.log_in("maciek@maciek.com", "password")

        assert "Too many failed login attempts." in my_account_page.get_error_meassage()