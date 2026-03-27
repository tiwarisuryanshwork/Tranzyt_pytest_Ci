from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    vietnam_country = (By.XPATH,"//div[contains(text(),'Vietnam')]")



    def select_country(self):
        self.driver.execute_script("window.scrollBy(0, 500)")
        self.wait.until(EC.element_to_be_clickable(self.vietnam_country)).click()