from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home_page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    contact_us = (By.XPATH, "//a[text()='Contact Us']")

    def click_contact_us(self):
        element = self.wait.until(EC.presence_of_element_located(self.contact_us))


        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        import time
        time.sleep(2)

        try:
            self.wait.until(EC.element_to_be_clickable(self.contact_us))
            element.click()
        except:

            self.driver.execute_script("arguments[0].click();", element)