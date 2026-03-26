from Testing.Automation.Pages.login_page import LoginPage


def test_login_flow(driver):
    login = LoginPage(driver)

    login.click_login()
    login.select_customer()
    login.enter_mobile_number("8840340000")
    login.click_send_otp()

    # Assertion (VERY IMPORTANT)
    assert "otp" in driver.page_source.lower()