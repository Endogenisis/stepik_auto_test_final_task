from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.Add_cart)
        add_button.click()
    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.Add_cart)
        add_button.click()
        self.solve_quiz_and_get_code()
        self.should_be_add_cart()
        self.should_be_price_cart()
    def should_be_add_cart(self):
        add_cart=self.browser.find_element(*ProductPageLocators.Add_cart_assert)
        text_add_cart = add_cart.text
        assert text_add_cart == self.browser.find_element(*ProductPageLocators.product_name).text, "Название товара не соответствует добавленному в корзину."
    def should_be_price_cart(self):
        cart_price = self.browser.find_element(*ProductPageLocators.cart_price)
        text_cart_price = cart_price.text
        assert text_cart_price == self.browser.find_element(*ProductPageLocators.price_product).text, "Сумма в корзине не соответствует цене."
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение появилось, но не должно."
    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение не исчезло."