import pytest

from config.config import URL
from config.config import USERNAME
from config.config import PASSWORD

from pages.login_page import LoginPage
from pages.leave_page import LeavePage


def test_assign_leave(driver):

    driver.get(URL)

    login = LoginPage(driver)

    login.login(USERNAME, PASSWORD)

    leave = LeavePage(driver)

    leave.open_assign_leave()

    leave.assign_leave(
        employee="Ranga Akunuri",
        leave_type="CAN - Vacation",
        from_date="2026-10-01",
        to_date="2026-10-03",
        comments="Automation Testing"
    )

    assert leave.leave_assigned_successfully()