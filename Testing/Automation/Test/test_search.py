from Testing.Automation.Home_page.search_feature import SearchPage


def test_check_search_filters(driver):
    search = SearchPage(driver)

    search.click_search_filter()
    search.put_value_filter("vietnam")
    search.click_country()