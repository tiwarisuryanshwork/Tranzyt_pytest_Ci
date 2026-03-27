import time

from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Theme_feature :
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)


    adventure_theme = (By.XPATH,"//img[contains(@src,'packagetype-images')]")
    # sun_sea_theme = (By.XPATH,"//img[@alt='Sun, Sand & Sea 🏖️']")
    # mountain_theme = (By.XPATH,"//img[@alt='Mountains & Mist 🏔️']")
    # island_theme  = (By.XPATH,"//img[@alt='Island Escapes 🌴']")
    # nature_theme = (By.XPATH,"//img[@alt='Nature & Serenity 🌿']")
    # culture_theme = (By.XPATH,"//img[@alt='Culture heritage🏛️']")


    def click_adventure(self):
        self.driver.execute_script("window.scrollBy(0, 800)")
        self.wait.until(EC.element_to_be_clickable(self.adventure_theme)).click()



    # def click_sun_sea(self):
    #     self.driver.execute_script("window.scrollBy(0, 800)")
    #     self.wait.until(EC.element_to_be_clickable(self.sun_sea_theme)).click()
    #
    #
    #
    # def click_mountain(self):
    #     self.driver.execute_script("window.scrollBy(0, 800)")
    #     self.wait.until(EC.element_to_be_clickable(self.mountain_theme)).click()
    #
    #
    #
    #
    # def click_island(self):
    #     self.driver.execute_script("window.scrollBy(0, 800)")
    #     self.wait.until(EC.element_to_be_clickable(self.island_theme)).click()
    #
    #
    #
    # def click_nature(self):
    #     self.driver.execute_script("window.scrollBy(0, 800)")
    #     self.wait.until(EC.element_to_be_clickable(self.nature_theme)).click()
    #
    #
    # def click_culture(self):
    #     self.driver.execute_script("window.scrollBy(0, 800)")
    #     self.wait.until(EC.element_to_be_clickable(self.culture_theme)).click()


time.sleep(5)