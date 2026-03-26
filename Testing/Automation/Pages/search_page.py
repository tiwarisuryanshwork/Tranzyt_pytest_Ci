import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait=WebDriverWait(driver,10)

    search_filter = (By.XPATH,"//input[@placeholder='Search destination, place, city...']")
    value_filter = (By.XPATH,"//input[@placeholder='Search destinations, cities, or experiences']")
    country_click = (By.XPATH,"//button[.//img[@alt='Vietnam']]")

    def click_search_filter (self):
        self.wait.until(EC.element_to_be_clickable(self.search_filter)).click()

    def put_value_filter(self,value):
        element = self.driver.find_element(*self.value_filter).send_keys(value)

    def click_country(self):
        self.wait.until(EC.element_to_be_clickable(self.country_click)).click()


time.sleep(3)