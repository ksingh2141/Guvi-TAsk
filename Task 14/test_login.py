from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage


class TestZen:

    valid_username = "kundansingh2141@gmail.com"
    valid_password = "Arcpk@8929"

    invalid_username = "wrong@gmail.com"
    invalid_password = "wrong123"


    # Successful login

    def test_successful_login(self,setup):

        driver = setup

        lp = LoginPage(driver)

        lp.login(
            self.valid_username,
            self.valid_password
        )

        lp.close_popup()

        assert driver.current_url == "https://www.zenclass.in/dashboard"


    # Unsuccessful login

    def test_unsuccessful_login(self,setup):

        driver=setup

        lp=LoginPage(driver)

        lp.login(
            self.invalid_username,
            self.invalid_password
        )

        assert "login" in driver.current_url


    # Validate username/password input

    def test_input_box(self,setup):

        driver=setup

        lp=LoginPage(driver)

        assert driver.find_element(*lp.username).is_displayed()

        assert driver.find_element(*lp.password).is_displayed()


    # Validate submit button

    def test_submit_button(self,setup):

        driver=setup

        lp=LoginPage(driver)

        assert driver.find_element(
            *lp.login_btn
        ).is_enabled()


    # Validate logout

    def test_logout(self, setup):
        driver = setup

        lp = LoginPage(driver)

        lp.login(
            self.valid_username,
            self.valid_password
        )

        lp.close_popup()

        lp.logout_user()

        WebDriverWait(driver, 10).until(
            lambda d: "login" in d.current_url
        )

        assert "login" in driver.current_url