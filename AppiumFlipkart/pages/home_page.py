# pages/home_page.py
import time

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def allow_permissions(self):
        try:
            allow_btn = self.driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
            allow_btn.click()
        except Exception:
            pass
        time.sleep(2)

    def skip_login(self):
        try:
            skip = self.driver.find_element(AppiumBy.ID, 'com.flipkart.android:id/custom_back_icon')
            skip.click()
        except Exception:
            pass
        time.sleep(2)

    def open_categories(self):
        try:
            category = self.driver.find_element(
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@content-desc="Categories"]/android.view.ViewGroup'
            )
            category.click()
            time.sleep(2)
            print("✅ Categories opened successfully")
            with allure.step("Opened Categories successfully"):
                pass
        except Exception as e:
            print(f"⚠️ Failed to open categories: {e}")
            # Take a screenshot and attach to Allure
            screenshot_file = "reports/screenshots/open_categories_error.png"
            self.driver.save_screenshot(screenshot_file)
            with allure.step("Failed to open Categories"):
                allure.attach.file(screenshot_file, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)

    def click_search_icon(self):
        try:
            search_icon = self.driver.find_element(
                AppiumBy.ID,
                'com.flipkart.android:id/search_icon'
            )
            search_icon.click()
            time.sleep(2)
            print("✅ Search icon clicked successfully")
            with allure.step("Clicked search icon successfully"):
                pass
        except Exception as e:
            print(f"⚠️ Failed to click search icon: {e}")
            # Take screenshot and attach to Allure
            screenshot_file = "reports/screenshots/click_search_icon_error.png"
            self.driver.save_screenshot(screenshot_file)
            with allure.step("Failed to click search icon"):
                allure.attach.file(
                    screenshot_file,
                    name="Search Icon Error",
                    attachment_type=allure.attachment_type.PNG
                )

    def search_product(self, product_name):
        try:
            # Find the search box and enter the product name
            search_box = self.driver.find_element(
                AppiumBy.XPATH,
                '//android.widget.EditText[@text="Search for products"]'
            )
            search_box.click()
            search_box.send_keys(product_name)
            # Press Enter key to search
            self.driver.press_keycode(66)
            time.sleep(3)
            print(f"✅ Searched for product: {product_name}")
            with allure.step(f"Searched for product: {product_name}"):
                pass
        except Exception as e:
            print(f"⚠️ Failed to search for product '{product_name}': {e}")
            # Take screenshot and attach to Allure
            screenshot_file = "reports/screenshots/search_product_error.png"
            self.driver.save_screenshot(screenshot_file)
            with allure.step("Failed to search product"):
                allure.attach.file(
                    screenshot_file,
                    name=f"Search Product Error - {product_name}",
                    attachment_type=allure.attachment_type.PNG
                )
