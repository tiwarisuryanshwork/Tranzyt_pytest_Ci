from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # 🔹 Locators
    login_button = (By.XPATH, "//button[text()='Login']")
    customer_option = (By.XPATH, "//p[text()='Customer']")
    mobile_inputs = (By.XPATH, "//input[contains(@placeholder,'Mobile')]")
    send_otp_btn = (By.XPATH, "//button[normalize-space()='Send OTP']")

    # 🔹 Actions

    def click_login(self):
        element = self.wait.until(
            EC.presence_of_element_located(self.login_button)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def select_customer(self):
        element = self.wait.until(
            EC.presence_of_element_located(self.customer_option)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)  # helps with animation issues
        self.driver.execute_script("arguments[0].click();", element)

    def enter_mobile_number(self, number):
        elements = self.driver.find_elements(*self.mobile_inputs)

        for el in elements:
            if el.is_displayed():
                el.clear()
                el.send_keys(number)
                break

    def click_send_otp(self):
        btn = self.wait.until(
            EC.presence_of_element_located(self.send_otp_btn)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", btn)