import time

from Testing.Automation.Home_page.themes_feature import Theme_feature


def test_click_adventures(driver):
    themes = Theme_feature (driver)



    themes.click_adventure()
    # themes.click_sun_sea()
    # themes.click_mountain()
    # themes.click_island()
    # themes.click_nature()
    # themes.click_culture()



time.sleep(3)