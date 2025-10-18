# PageObject/SortingPage.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SortingPage:
    # --- Locators ---
    sort_dropdown = (AppiumBy.ACCESSIBILITY_ID, "test-Selector")
    price_labels = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'$')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def sort_by_price_low_to_high(self):
        """
        Opens the sort dropdown and selects 'Price (low to high)'.
        Works for both Android and iOS (Appium selectors).
        """
        dropdown = self.wait.until(EC.element_to_be_clickable(self.sort_dropdown))
        dropdown.click()

        # Select the 'Price (low to high)' option
        # Use text-based search for dynamic UI
        option = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Price (low to high)")')
            )
        )
        option.click()

    def get_all_prices(self):

        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.price_labels)
        )
        prices = []
        for element in elements:
            text = element.text.replace("$", "").strip()
            try:
                prices.append(float(text))
            except ValueError:
                pass  # ignore any non-numeric text
        return prices
