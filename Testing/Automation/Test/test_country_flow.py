import time

import pytest

from Testing.Automation.Country_page.country_page import CountryPage
from Testing.Automation.Country_page.home_page import HomePage
from Testing.Automation.Country_page.package_page import PackagePage


def test_package_details_flow(driver):
    home = HomePage(driver)
    country = CountryPage(driver)
    package = PackagePage(driver)

    home.select_country()
    country.click_explore_packages()
    package.click_view_details()