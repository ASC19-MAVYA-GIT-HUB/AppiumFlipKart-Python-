# tests/test_search_item.py
import pytest
import allure
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from utils.excel_utils import ExcelUtils  # Make sure utils folder has __init__.py

@pytest.mark.usefixtures("setup")
class TestSearchItem:

    @allure.feature("Search Functionality")
    @allure.story("Search for product from Excel and apply filters")
    def test_search_watch(self):
        # Read product name from Excel
        excel = ExcelUtils("Book1.xlsx")
        search_item = excel.get_cell_value("Sheet1", "A1")

        home = HomePage(self.driver)
        results = SearchResultsPage(self.driver)

        with allure.step("Allow permissions and skip login"):
            home.allow_permissions()
            home.skip_login()

        with allure.step("Open categories and search product"):
            home.open_categories()
            home.click_search_icon()
            home.search_product(search_item)

        with allure.step("Dismiss popups and apply filters"):
            results.dismiss_not_now()
            results.open_filter()
            results.apply_brand_filter("Titan")
            results.apply_price_filter("20001")
            results.apply_filter()

        with allure.step("Scroll results and verify brand"):
            results.scroll_results()
            results.verify_brand("Titan")

        with allure.step("Select product and take screenshot"):
            results.select_watch()
            results.take_screenshot("final_result.png")
            allure.attach.file(
                "final_result.png",
                name="Final Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
