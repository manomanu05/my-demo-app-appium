import pytest
import os
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from PageObject.LoginPage import LoginPage
from Utilities.ReadConfig import ReadConfig
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Cart_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_add_to_cart_and_verify(self, setup):
        driver = setup
        wait = WebDriverWait(driver, 20)

        # --- LOGIN ---
        lp = LoginPage(driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()

        # Handle app pop-up (e.g., password change alert)
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass

        # --- ADD PRODUCT TO CART ---
        try:
            first_product_name_element = wait.until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Item title"))
            )
            product_name = first_product_name_element.text
        except TimeoutException:
            pytest.fail(" Product name not found on product list page")

        # Click add-to-cart button (for that product)
        add_to_cart_btn = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "test-ADD TO CART"))
        )
        add_to_cart_btn.click()

        # --- OPEN CART ---
        cart_icon = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "test-Cart"))
        )
        cart_icon.click()

        # --- VERIFY PRODUCT IN CART ---
        try:
            cart_product_name_element = wait.until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Item title"))
            )
            cart_product_name = cart_product_name_element.text
        except TimeoutException:
            pytest.fail(" Could not find product in cart")

        assert product_name == cart_product_name, (
            f" Product mismatch! Expected '{product_name}' but found '{cart_product_name}' in cart."
        )

        print(f" Added product: {product_name}, Cart product: {cart_product_name}")

        # --- TAKE SCREENSHOT ---
        os.makedirs("Screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"Screenshots/cart_verification_{timestamp}.png"
        driver.save_screenshot(screenshot_path)

        driver.quit()
