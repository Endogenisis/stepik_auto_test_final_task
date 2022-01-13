from .base_page import BasePage
from .locators import LoginPageLocators

# Файл проверок и посика элементов на странице логина.

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print("Проверка страницы логина.")
        assert "login" in self.browser.current_url,  "Это не страница логина."
        # реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        # Проверка наличия формы логина
        assert self.is_element_present(*LoginPageLocators.Login_form), "Нет формы логина."

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.Register_form), "Нет формы регистрации."