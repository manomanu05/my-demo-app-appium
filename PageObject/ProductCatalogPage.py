# PageObject/ProductCatalogPage.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductCatalogPage:
    # Prefer stable locators: accessibility_id, resource-id, or content-desc
    catalog_title_id = "test-CATALOG_TITLE"
    first_product_accessibility_id = "test-Item title"
    add_to_cart_btn_accessibility_id = "test-ADD TO CART"
    cart_icon_accessibility_id = "test-Cart"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def get_catalog_title(self):
        element = self.wait.until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, self.catalog_title_id))
        )
        return element.text

    def open_first_product(self):
        product = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, self.first_product_accessibility_id))
        )
        product.click()

    def add_first_product_to_cart(self):
        add_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, self.add_to_cart_btn_accessibility_id))
        )
        add_button.click()

    def open_cart(self):
        cart_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, self.cart_icon_accessibility_id))
        )
        cart_button.click()
