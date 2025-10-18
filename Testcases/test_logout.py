import pytest
from PageObject.LoginPage import LoginPage
from Utilities.ReadConfig import ReadConfig
from selenium.common.exceptions import NoAlertPresentException
import os
from Utilities.Screenshot import take_screenshot


class Test_Logout_003:
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_logout(self, setup):
        driver = setup
        lp = LoginPage(driver)

        # --- Perform login ---
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()

        # --- Handle Chrome Security Alert (if any) ---
        try:
            driver.switch_to.alert.accept()
        except NoAlertPresentException:
            pass

        # --- Click Menu and Logout ---
        try:
            lp.clickMenu()
            lp.clickLogout()
        except Exception as e:
            take_screenshot(driver, "logout_error")
            pytest.fail(f"Logout failed due to: {str(e)}")

        # --- Handle Alert if present after logout ---
        try:
            driver.switch_to.alert.accept()
        except NoAlertPresentException:
            pass

        # --- Verification ---
        # Wait for login button to reappear after logout
        try:
            driver.find_element("accessibility id", "test-LOGIN")
            logout_success = True
        except:
            logout_success = False

        # --- Screenshot and Assertion ---
        os.makedirs("Screenshots", exist_ok=True)
        screenshot_path = "Screenshots/test_logout.png"
        driver.save_screenshot(screenshot_path)

        assert logout_success, "Logout failed - screenshot saved at {}".format(screenshot_path)
