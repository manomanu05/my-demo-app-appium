import pytest
import os
from datetime import datetime
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from PageObject.LoginPage import LoginPage
from PageObject.SortingPage import SortingPage
from Utilities.ReadConfig import ReadConfig

class Test_Sorting_007:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_sort_by_price_low_to_high(self, setup):
        driver = setup

        # --- LOGIN ---
        lp = LoginPage(driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        print(" Login successful")

        # Handle alert after login (if any)
        try:
            alert = driver.switch_to.alert
            alert.accept()
            print(" Alert accepted")
        except NoAlertPresentException:
            pass

        # --- SORT PRODUCTS BY PRICE (Low to High) ---
        sp = SortingPage(driver)
        try:
            sp.sort_by_price_low_to_high()
            prices = sp.get_all_prices()
            assert prices == sorted(prices), " Products are NOT sorted by price low to high"
            print(" Products sorted by price (Low to High):", prices)

            # Take screenshot on success
            os.makedirs("Screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            driver.save_screenshot(f"Screenshots/sort_success_{timestamp}.png")

        except TimeoutException:
            os.makedirs("Screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            driver.save_screenshot(f"Screenshots/sort_failed_{timestamp}.png")
            pytest.fail(" Sorting verification failed. Screenshot taken.")

        driver.quit()
