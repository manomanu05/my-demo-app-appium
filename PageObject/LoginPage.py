from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # --- Locators (update if app element IDs differ) ---
    textbox_username_id = "test-Username"
    textbox_password_id = "test-Password"
    button_login_id = "test-LOGIN"
    error_message_id = "test-Error message"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # --- Login Actions ---
    def setUsername(self, username):
        username_field = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, self.textbox_username_id))
        )
        username_field.clear()
        username_field.send_keys(username)

    def setPassword(self, password):
        password_field = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, self.textbox_password_id))
        )
        password_field.clear()
        password_field.send_keys(password)

    def clickLogin(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, self.button_login_id))
        )
        login_button.click()

    # --- Error Handling ---
    def get_error_text(self):
        try:
            error_element = self.wait.until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, self.error_message_id))
            )
            return error_element.text.strip()
        except:
            return ""  # No error message found
