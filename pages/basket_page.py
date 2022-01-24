from .base_page import BasePage
from .locators import BasketPageLocators
class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.not_empty_basket), \
            "Корзина не пуста."
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.empty_basket), \
            "Нет сообщения о пустой корзине."