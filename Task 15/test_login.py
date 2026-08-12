from pages.login_page import LoginPage
from utilities.excel_utils import ExcelUtils


class TestLoginDDT:

    file = "testdata/LoginData.xlsx"
    sheet = "Sheet1"

    def test_login_ddt(self, setup):

        driver = setup

        rows = ExcelUtils.get_row_count(
            self.file,
            self.sheet
        )

        for r in range(2, rows + 1):

            username = ExcelUtils.read_data(
                self.file,
                self.sheet,
                r,
                2
            )

            password = ExcelUtils.read_data(
                self.file,
                self.sheet,
                r,
                3
            )

            driver.get(
                "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
            )

            lp = LoginPage(driver)

            lp.enter_username(username)
            lp.enter_password(password)
            lp.click_login()

            if lp.is_login_successful():

                ExcelUtils.update_test_result(
                    self.file,
                    self.sheet,
                    r,
                    "Passed"
                )

                lp.logout()

            else:

                ExcelUtils.update_test_result(
                    self.file,
                    self.sheet,
                    r,
                    "Failed"
                )
