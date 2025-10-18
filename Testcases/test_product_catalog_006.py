import pytest
import os
from datetime import datetime
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from PageObject.LoginPage import LoginPage
from PageObject.ProductCatalogPage import ProductCatalogPage
from Utilities.ReadConfig import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_ProductCatalog_006:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_product_catalog(self, setup):
        driver = setup
        wait = WebDriverWait(driver, 20)

        # --- LOGIN ---
        lp = LoginPage(driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        print(" Login successful")

        # Handle any alert (e.g., browser/app pop-ups)
        try:
            alert = driver.switch_to.alert
            alert.accept()
            print(" Alert accepted")
        except NoAlertPresentException:
            pass

        # --- PRODUCT CATALOG TEST ---
        pc = ProductCatalogPage(driver)
        try:
            catalog_title = pc.get_catalog_title()
            assert catalog_title == "Products", "Catalog page not loaded correctly"
        except TimeoutException:
            os.makedirs("Screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"Screenshots/catalog_page_failed_{timestamp}.png"
            driver.save_screenshot(screenshot_path)
            pytest.fail(" Catalog page not loaded. Screenshot taken.")

        # Open first product and get details
        try:
            pc.open_first_product()
            product_name = pc.get_product_name()
            product_price = pc.get_product_price()
            print(f"🛍️ Product Name: {product_name}, Price: {product_price}")

            # Screenshot for successful product load
            os.makedirs("Screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"Screenshots/catalog_success_{timestamp}.png"
            driver.save_screenshot(screenshot_path)

        except TimeoutException:
            os.makedirs("Screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"Screenshots/product_load_failed_{timestamp}.png"
            driver.save_screenshot(screenshot_path)
            pytest.fail(" Could not open product or fetch details. Screenshot taken.")

        driver.quit()
