from playwright.sync_api import TimeoutError


class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = page.locator("input[type='text']")
        self.password = page.locator("input[type='password']")
        self.login_btn = page.locator("button[type='submit']")

    def open_url(self, url):
        self.page.goto(url)

    def enter_username(self, username):
        self.username.fill(username)

    def enter_password(self, password):
        self.password.fill(password)

    def click_login(self):
        self.login_btn.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def validate_username_box(self):
        return self.username.is_visible()

    def validate_password_box(self):
        return self.password.is_visible()

    def validate_submit_button(self):
        return self.login_btn.is_enabled()

    def close_popup(self):
        try:
            popup = self.page.locator(
                "button[aria-label='Close popup']"
            )

            if popup.count() > 0:
                popup.click(force=True)
                print("Popup closed")
            else:
                print("Popup not displayed")

        except Exception as e:
            print(f"Popup error: {e}")