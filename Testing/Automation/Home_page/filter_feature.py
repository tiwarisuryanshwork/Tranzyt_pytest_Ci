import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Filter_explore:
    def __init__(self,driver):
        self.driver = driver
        self.wait =WebDriverWait(driver,10)

    # family_filter = (By.XPATH,"//img[contains(@src,'F4.png')]")
    # honeymoon_filter = (By.XPATH,"//button[.//img[contains(@src,'Frame_2147223650.png')]]")
    # solo_filter = (By.XPATH,"//button[normalize-space()='Solo']")
    friend_filter = (By.XPATH,"//button[normalize-space()='Friends']")




    # def click_family(self):
    #     self.wait.until(EC.element_to_be_clickable(self.family_filter)).click()
    #
    # def click_honeymoon(self):
    #     self.wait.until(EC.element_to_be_clickable(self.honeymoon_filter)).click()
    #
    # def click_solo(self):
    #     self.wait.until(EC.element_to_be_clickable(self.solo_filter)).click()

    def click_friends(self):
        self.wait.until(EC.element_to_be_clickable(self.friend_filter)).click()

time.sleep(5)