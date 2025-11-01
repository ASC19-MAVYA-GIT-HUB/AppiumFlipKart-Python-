# # tests/conftest.py
# import os
# import pytest
# from datetime import datetime
# from base.base_driver import BaseDriver
#
# @pytest.fixture(scope="class")
# def setup(request):
#     base = BaseDriver()
#     driver = base.start_driver()
#     request.cls.driver = driver
#     yield
#     base.quit_driver()
#
#
# # ---------- Extent Report Configuration ----------
#
# def pytest_configure(config):
#     # Create report folder if it doesn't exist
#     if not os.path.exists("reports"):
#         os.makedirs("reports")
#
#     # Timestamped report filename
#     report_name = datetime.now().strftime("report_%Y-%m-%d_%H-%M-%S.html")
#     config.option.htmlpath = os.path.join("reports", report_name)
#
#     config._metadata = {
#         "Project Name": "Flipkart App Automation",
#         "Module Name": "Search Item",
#         "Tester": "Varun"
#     }
#
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionfinish(session, exitstatus):
#     print("\n\n✅ Test Execution Completed. Report generated in 'reports/' folder.\n")
#
#
# # ---------- Attach Screenshots on Failure ----------
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call, pytest_html=None):
#     """
#     Attach screenshot to the HTML report on test failure.
#     """
#     outcome = yield
#     rep = outcome.get_result()
#
#     if rep.when == "call" and rep.failed:
#         driver = getattr(item.cls, "driver", None)
#         if driver:
#             screenshot_dir = "reports/screenshots"
#             os.makedirs(screenshot_dir, exist_ok=True)
#
#             file_name = f"{item.name}_{datetime.now().strftime('%H-%M-%S')}.png"
#             destination = os.path.join(screenshot_dir, file_name)
#             driver.save_screenshot(destination)
#             if "pytest_html" in item.config.pluginmanager.list_name_plugin():
#                 # Attach screenshot to HTML report
#                 extra = getattr(rep, "extra", [])
#                 extra.append(pytest_html.extras.image(destination))
#                 rep.extra = extra
# # conftest.py
# def pytest_sessionfinish(session, exitstatus):
#     print("\n\nTest Execution Completed. Report generated.\n")

# tests/conftest.py
import os
import pytest
from datetime import datetime
from base.base_driver import BaseDriver
import allure

@pytest.fixture(scope="class")
def setup(request):
    base = BaseDriver()
    driver = base.start_driver()
    request.cls.driver = driver
    yield
    base.quit_driver()

# ---------- Attach screenshots on failure ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Attach screenshot to Allure report on test failure.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = getattr(item.cls, "driver", None)
        if driver:
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = f"{item.name}_{datetime.now().strftime('%H-%M-%S')}.png"
            file_path = os.path.join(screenshot_dir, file_name)
            driver.save_screenshot(file_path)

            # Attach screenshot to Allure report
            allure.attach.file(file_path, name=item.name, attachment_type=allure.attachment_type.PNG)
