from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CountactUs:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    full_name=(By.XPATH,"//input[@name='fullName']")
    email=(By.XPATH,"//input[@name='email']")
    phone=(By.XPATH,"//input[@name='phone']")
    message=(By.XPATH,"//textarea[@name='message']")
    sumbit=(By.XPATH,"//button[text()='Submit']")

    def name_value(self):
        self.wait.until(EC.visibility_of_element_located(self.full_name)).send_keys("Suryansh")

    def email_value(self):
        self.wait.until(EC.visibility_of_element_located(self.email)).send_keys("demo@gmail.co")

    def phone_value(self):
        self.driver.execute_script("window.scrollTo(0,300)")
        self.wait.until(EC.visibility_of_element_located(self.phone)).send_keys("123456")

    def message_value(self):
        self.wait.until(EC.visibility_of_element_located(self.message)).send_keys("hey lets start testing")

    def click_sumbit(self):
        self.wait.until(EC.element_to_be_clickable(self.sumbit)).click()