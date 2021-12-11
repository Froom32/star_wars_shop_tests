from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://kfund.github.io/test-shop/"

    def find_element(self, xpath, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.XPATH, xpath)),
                                                      message=f"Can't find element by locator {xpath}")

    def click(self, xpath):
        return self.find_element(xpath).click()

    def go_to_site(self):
        return self.driver.get(self.base_url)
