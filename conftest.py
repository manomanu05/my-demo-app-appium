from appium import webdriver
from Utilities.ReadConfig import ReadConfig
import pytest

@pytest.fixture(scope="class")
def setup(request):
    desired_caps = {
        "platformName": ReadConfig.getPlatformName(),  # e.g., "Android"
        "appium:platformVersion": ReadConfig.getPlatformVersion(),  # e.g., "16"
        "appium:deviceName": ReadConfig.getDeviceName(),  # e.g., "emulator-5554"
        "appium:app": ReadConfig.getAppPath(),  # full path to APK
        "appium:automationName": "UiAutomator2",
        "appium:noReset": True,
        "appium:newCommandTimeout": 300,
        "appium:appPackage": "com.swaglabsmobileapp",
        "appium:appActivity": "com.swaglabsmobileapp.MainActivity",
        "appium:appWaitActivity": "com.swaglabsmobileapp.MainActivity"
    }

    # Appium server URL (adjust port if needed)
    driver = webdriver.Remote("http://localhost:4724/wd/hub", {"capabilities": {"alwaysMatch": desired_caps, "firstMatch": [{}]}})
    request.cls.driver = driver
    yield driver
    driver.quit()