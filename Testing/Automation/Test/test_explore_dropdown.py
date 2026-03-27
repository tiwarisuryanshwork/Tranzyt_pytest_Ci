import time

from Testing.Automation.Home_page.explore_dropdown import ExploreNavbar


def test_explore_navbar(driver):
    dropdown = ExploreNavbar(driver)


    dropdown.click_explore()
    dropdown.click_countrys()
    dropdown.click_packages()