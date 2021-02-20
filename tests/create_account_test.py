import random
import pytest
from pages.my_account_page import MyAccountPage

# maciek@maciek.com
# MaciekMacie
# monika@monika.com
# MonikaMonik

@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_creating_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page_my_account()
        my_account_page.create_account("maciek@maciek.com", "MaciekMacie")

        msg = "Error: An account is already registered with your email address. Please log in."
        assert msg in my_account_page.get_error_meassage()

    def test_creating_account_passed(self):
        email = str(random.randint(0,1000))+ "maciek@maciek.com"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page_my_account()
        my_account_page.create_account(email, "MaciekMacie")

        assert my_account_page.is_logout_link_displayed()
