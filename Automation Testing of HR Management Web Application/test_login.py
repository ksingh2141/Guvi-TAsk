from pages.login_page import LoginPage
from utilities.excel_utils import ExcelUtils

from config.config import URL


def test_login_ddt(driver):

    excel = ExcelUtils("data/LoginData.xlsx")

    login = LoginPage(driver)

    rows = excel.row_count()

    for row in range(2, rows + 1):

        username = excel.read_data(row, 1)

        password = excel.read_data(row, 2)

        expected = excel.read_data(row, 3)

        driver.get(URL)

        login.login(username, password)

        if expected == "Pass":

            assert login.is_login_successful()

            login.logout()

            excel.write_data(row, 4, "PASS")

        else:

            assert "Invalid" in login.get_error_message()

            excel.write_data(row, 4, "PASS")