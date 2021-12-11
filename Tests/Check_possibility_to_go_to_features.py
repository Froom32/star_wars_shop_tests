from Pages.HomePage import HomePageHelper


def test_possibility_to_go_to_features(browser):
    home_page = HomePageHelper(browser)
    home_page.go_to_site()
    home_page.click("/html/body/nav/div/div/div[1]/div[1]/a[2]")
    home_page.click("/html/body/main/div/div[2]/div[1]/div/div[2]/button")
