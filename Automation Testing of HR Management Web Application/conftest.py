import pytest

from config.config import BROWSER
from utilities.browser_factory import BrowserFactory
from utilities.logger import LogGenerator


logger = LogGenerator.loggen()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=BROWSER,
        help="Browser Name"
    )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            path = (
                f"reports/screenshots/"
                f"{item.name}_failure.png"
            )

            driver.save_screenshot(path)

            print(
                f"\nFailure Screenshot: {path}"
            )
@pytest.fixture(scope="function")
def driver(request):

    browser = request.config.getoption("--browser")

    logger.info(f"Launching Browser : {browser}")

    driver = BrowserFactory.get_driver(browser)

    yield driver

    logger.info("Closing Browser")

    driver.quit()