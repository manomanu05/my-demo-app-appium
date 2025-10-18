from appium import webdriver
from Utilities.ReadConfig import ReadConfig
import pytest

@pytest.fixture(scope="class")
def setup(request):
    desired_caps = {
        "platformName": ReadConfig.getPlatformName(),
        "platformVersion": ReadConfig.getPlatformVersion(),
        "deviceName": ReadConfig.getDeviceName(),
        "app": ReadConfig.getAppPath(),
        "automationName": "UiAutomator2",
        "noReset": True
    }

    driver = webdriver.Remote(ReadConfig.getAppiumServer(), desired_caps)
    request.cls.driver = driver
    yield driver
    driver.quit()
