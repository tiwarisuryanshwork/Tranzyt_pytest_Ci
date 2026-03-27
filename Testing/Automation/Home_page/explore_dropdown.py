import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExploreNavbar:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    explore = (By.XPATH,"//p[text()='Explore']")
    click_country = (By.XPATH,"//li//p[text()='Vietnam']")
    click_package = (By.XPATH,"//h3[contains(text(),'Escape to Vietnam')]")


    def click_explore(self):
        self.wait.until(EC.element_to_be_clickable(self.explore)).click()

    def click_countrys(self):
        self.wait.until(EC.element_to_be_clickable(self.click_country)).click()

    def click_packages(self):
        self.wait.until(EC.element_to_be_clickable(self.click_package)).click()


time.sleep(10)