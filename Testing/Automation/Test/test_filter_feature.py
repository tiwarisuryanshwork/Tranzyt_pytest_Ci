from Testing.Automation.Home_page.filter_feature import Filter_explore


def test_click_family(driver):
    action = Filter_explore(driver)

    # action.click_family()
    # action.click_honeymoon()
    action.click_friends()
    # action.click_solo()