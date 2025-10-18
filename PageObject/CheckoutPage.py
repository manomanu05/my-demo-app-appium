# PageObject/CheckoutPage.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CheckoutPage:
    # --- Locators (using stable accessibility IDs or resource IDs) ---
    add_to_cart_btn = (AppiumBy.ACCESSIBILITY_ID, "test-ADD TO CART")
    cart_icon = (AppiumBy.ACCESSIBILITY_ID, "test-Cart")
    checkout_btn = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT")
    first_name_field = (AppiumBy.ACCESSIBILITY_ID, "test-First Name")
    last_name_field = (AppiumBy.ACCESSIBILITY_ID, "test-Last Name")
    postal_code_field = (AppiumBy.ACCESSIBILITY_ID, "test-Zip/Postal Code")
    continue_btn = (AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE")
    finish_btn = (AppiumBy.ACCESSIBILITY_ID, "test-FINISH")
    completion_text = (AppiumBy.ACCESSIBILITY_ID, "test-COMPLETE_HEADER")
    popup_close_btn = (AppiumBy.ACCESSIBILITY_ID, "test-Close")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # --- Actions ---
    def add_product_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart_btn)).click()

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.checkout_btn)).click()

    def fill_checkout_information(self, first_name, last_name, postal_code):
        # Handle any app popup
        try:
            popup = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(self.popup_close_btn)
            )
            popup.click()
        except TimeoutException:
            pass

        # Fill checkout details
        self.wait.until(EC.visibility_of_element_located(self.first_name_field)).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.postal_code_field).send_keys(postal_code)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_btn)).click()

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.finish_btn)).click()

    def get_completion_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.completion_text)).text
