from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.Add_cart)
        add_button.click()
        self.solve_quiz_and_get_code()
