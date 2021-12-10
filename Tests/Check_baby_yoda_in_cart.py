from Pages.HomePage import HomePageHelper


def test_baby_yoda_should_present_in_cart(browser):
    home_page = HomePageHelper(browser)
    home_page.go_to_site()
    home_page.click("/html/body/main/div/div/div[3]/div/div/div/button")
    assert home_page.check_first_element_in_cart() == "BABY YODA"
