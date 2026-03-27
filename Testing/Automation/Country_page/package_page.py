from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PackagePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    view_details = (By.XPATH, "//button[contains(text(),'View Details')]")

    def click_view_details(self):
        self.wait.until(EC.element_to_be_clickable(self.view_details)).click()