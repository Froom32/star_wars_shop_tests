from Pages.BasePage import BasePage


class HomePageSearchLocators:
    XPATH_BUTTON_CART = "/html/body/nav/div/div/div[1]/div[1]/span"
    XPATH_FIRST_GOOD_IN_CART = "/html/body/div[1]/div/div/div[2]/ul[1]/li/div[1]"


class HomePageHelper(BasePage):

    def check_first_element_in_cart(self):
        self.click(HomePageSearchLocators.XPATH_BUTTON_CART)
        return self.find_element(HomePageSearchLocators.XPATH_FIRST_GOOD_IN_CART).text
