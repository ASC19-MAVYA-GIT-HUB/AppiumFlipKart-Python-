
import time

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# pages/search_results_page.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def dismiss_not_now(self):
        try:
            not_now = self.driver.find_element(AppiumBy.ID, 'com.flipkart.android:id/not_now_button')
            not_now.click()
        except Exception:
            pass
        time.sleep(2)

    def open_filter(self):
        try:
            filter_btn = self.driver.find_element(
                AppiumBy.XPATH,
                '//android.widget.TextView[@text="Filter"]'
            )
            filter_btn.click()
            time.sleep(2)
            print("✅ Filter button clicked successfully")
            with allure.step("Clicked Filter button successfully"):
                pass
        except Exception as e:
            print(f"⚠️ Failed to click Filter button: {e}")
            # Take screenshot and attach to Allure
            screenshot_file = "reports/screenshots/open_filter_error.png"
            self.driver.save_screenshot(screenshot_file)
            with allure.step("Failed to click Filter button"):
                allure.attach.file(
                    screenshot_file,
                    name="Filter Button Error",
                    attachment_type=allure.attachment_type.PNG
                )

    def apply_brand_filter(self, brand_name="Titan"):
        try:
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Brand")').click()
            brand = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("{brand_name}"))'
                ))
            )
            brand.click()
            print(f"✅ Selected {brand_name} brand")
        except TimeoutException:
            print(f"⚠️ {brand_name} brand not found")

    def apply_price_filter(self, price_keyword="20001"):
        try:
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Price")').click()
            price = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("{price_keyword}"))'
                ))
            )
            price.click()
            print(f"✅ Selected price containing {price_keyword}")
        except TimeoutException:
            print("⚠️ Price range not found")

    def apply_filter(self):
        try:
            apply_btn = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("Filter")'
            )
            apply_btn.click()
            time.sleep(2)
            print("✅ Applied filter successfully")
            with allure.step("Applied filter successfully"):
                pass
        except Exception as e:
            print(f"⚠️ Failed to apply filter: {e}")
            # Take screenshot and attach to Allure
            screenshot_file = "reports/screenshots/apply_filter_error.png"
            self.driver.save_screenshot(screenshot_file)
            with allure.step("Failed to apply filter"):
                allure.attach.file(
                    screenshot_file,
                    name="Apply Filter Error",
                    attachment_type=allure.attachment_type.PNG
                )

    def verify_brand(self, brand_name="Titan"):
        try:
            text_data = self.driver.find_element(
                AppiumBy.XPATH,
                f'(//android.widget.TextView[@text="{brand_name}"])[1]'
            )
            assert brand_name in text_data.text
            print(f"✅ Brand '{brand_name}' found")
            with allure.step(f"Verified brand: {brand_name}"):
                pass
        except Exception as e:
            print(f"⚠️ Unexpected error in verifying brand '{brand_name}': {e}")
            screenshot_file = f"reports/screenshots/verify_brand_error.png"
            self.driver.save_screenshot(screenshot_file)
            with allure.step("Unexpected error during brand verification"):
                allure.attach.file(
                    screenshot_file,
                    name="Brand Verification Error",
                    attachment_type=allure.attachment_type.PNG
                )

    def scroll_results(self, scroll_count=1):
        try:
            for i in range(scroll_count):
                self.driver.swipe(start_x=500, start_y=1200, end_x=500, end_y=400, duration=800)
                print(f"✅ Scrolled {i + 1} time(s)")
                with allure.step(f"Scrolled {i + 1} time(s)"):
                    pass
                time.sleep(2)
        except Exception as e:
            print(f"⚠️ Unexpected error while scrolling: {e}")
            screenshot_file = f"reports/screenshots/scroll_results_unexpected_error.png"
            self.driver.save_screenshot(screenshot_file)
            with allure.step("Unexpected error while scrolling"):
                allure.attach.file(
                    screenshot_file,
                    name="Scroll Results Unexpected Error",
                    attachment_type=allure.attachment_type.PNG
                )

    def select_watch(self):
        try:
            watch_name = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true))'
                    '.scrollIntoView(new UiSelector().textContains("Edge Ceramic Quartz in Glossy Green Dial Analog Watch"))'
                ))
            )
            watch_name.click()
            print("✅ Watch selected successfully")
            time.sleep(5)

        except TimeoutException:
            print("⚠️ Product name element not found. Maybe page took longer to load.")

    def take_screenshot(self, filename):
        time.sleep(3)
        self.driver.get_screenshot_as_file(filename)
        print(f"✅ Screenshot saved: {filename}")
