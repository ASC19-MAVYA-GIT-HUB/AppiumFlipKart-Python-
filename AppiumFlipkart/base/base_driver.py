# base/base_driver.py
from appium import webdriver
from appium.options.common import AppiumOptions
from typing import Dict, Any

class BaseDriver:
    def __init__(self):
        self.driver = None

    def start_driver(self) -> None:
        caps: Dict[str, Any] = {
            "platformName": "Android",
            "deviceName": "emulator-5554",  # or "Android Emulator"
            "platformVersion": "13",         # Must correspond to the emulator OS version
            "appPackage": "com.flipkart.android",
            "appActivity": "com.flipkart.android.activity.HomeFragmentHolderActivity",
            "automationName": "UiAutomator2",
            "noReset": True,
            "newCommandTimeout": 3600,
            "connectHardwareKeyboard": True
        }

        url = 'http://localhost:4723'
        self.driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(caps))
        self.driver.implicitly_wait(10)
        return self.driver

    def quit_driver(self) -> None:
        if self.driver:
            self.driver.quit()
