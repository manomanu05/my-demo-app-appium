import pytest
import os
from datetime import datetime
from PageObject.LoginPage import LoginPage
from Utilities.ReadConfig import ReadConfig
from Utilities.Screenshot import take_screenshot


class Test_002_InvalidLogin:
    username_list = ["invalid_user1", "invalid_user2", "invalid_user3"]
    password = ReadConfig.getPassword()

    @pytest.mark.regression
    def test_login_invalid(self, setup):
        driver = setup
        lp = LoginPage(driver)

        os.makedirs("Screenshots", exist_ok=True)

        for username in self.username_list:
            lp.setUsername(username)
            lp.setPassword(self.password)
            lp.clickLogin()

            # Wait for error message
            error_text = lp.get_error_text()

            # Screenshot path
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"Screenshots/invalid_login_{username}_{timestamp}.png"

            # Save screenshot for each iteration
            driver.save_screenshot(screenshot_path)

            # Assertion based on expected error
            if error_text:
                print(f"✅ Invalid login correctly blocked for: {username}")
                print(f"Error Message: {error_text}")
                assert (
                    "Epic sadface" in error_text
                    or "locked" in error_text
                    or "Username and password" in error_text
                ), f"Unexpected error message: {error_text}"
            else:
                take_screenshot(driver, f"no_error_{username}")
                assert False, f"No error message displayed for invalid user: {username}"

            # Clear username and password fields for next iteration
            lp.clear_username()
            lp.clear_password()
