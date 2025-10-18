import pytest
import os
from datetime import datetime
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from PageObject.LoginPage import LoginPage
from PageObject.CheckoutPage import CheckoutPage
from Utilities.ReadConfig import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Checkout_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_complete_checkout_flow(self, setup):
        driver = setup
        wait = WebDriverWait(driver, 20)

        # --- LOGIN ---
        lp = LoginPage(driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        print("Login successful")

        # --- HANDLE APP ALERT (IF ANY) ---
        try:
            alert = driver.switch_to.alert
            alert.accept()
            print(" Alert accepted")
        except NoAlertPresentException:
            pass

        # --- PRODUCT / CART / CHECKOUT FLOW ---
        checkout = CheckoutPage(driver)

        # Add product
        try:
            checkout.add_product_to_cart()
        except TimeoutException:
            pytest.fail(" Could not find Add-to-Cart button")

        # Open cart
        try:
            checkout.open_cart()
        except TimeoutException:
            pytest.fail(" Could not open cart")

        # Click checkout
        try:
            checkout.click_checkout()
        except TimeoutException:
            pytest.fail(" Could not click checkout")

        # Fill checkout info
        try:
            checkout.fill_checkout_information("John", "Doe", "560001")
        except TimeoutException:
            pytest.fail(" Could not fill checkout information")

        # Continue and finish
        try:
            checkout.click_continue()
            checkout.click_finish()
        except TimeoutException:
            pytest.fail(" Could not complete checkout")

        # --- VALIDATION ---
        try:
            completion_text = checkout.get_completion_text()
            assert completion_text == "Thank you for your order!", " Order not completed successfully"
            print(" Order completed successfully")
        except TimeoutException:
            # Screenshot on failure
            os.makedirs("Screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"Screenshots/checkout_failed_{timestamp}.png"
            driver.save_screenshot(screenshot_path)
            pytest.fail(" Checkout completion text not found. Screenshot taken.")

        # Take screenshot on success
        os.makedirs("Screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"Screenshots/checkout_success_{timestamp}.png"
        driver.save_screenshot(screenshot_path)

        driver.quit()
