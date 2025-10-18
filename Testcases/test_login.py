import pytest
import os
from PageObject.LoginPage import LoginPage
from Utilities.ReadConfig import ReadConfig


class Test_001_Login:
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login_valid(self, setup):
        driver = setup

        lp = LoginPage(driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()

        # Create Screenshots folder if not exists
        os.makedirs("Screenshots", exist_ok=True)
        screenshot_path = "Screenshots/test_login.png"

        try:
            # Verify successful login — you can modify this locator per app
            inventory_locator = ("accessibility id", "test-Cart")
            success = False
            try:
                driver.find_element(*inventory_locator)
                success = True
            except:
                success = False

            driver.save_screenshot(screenshot_path)

            assert success, "Login failed - Screenshot saved at {}".format(screenshot_path)
        finally:
            driver.quit()
