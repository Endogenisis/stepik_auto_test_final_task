from .base_page import BasePage
from .locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from .login_page import LoginPage
# Файл поиска элементов на главной странице.
class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        # return LoginPage(browser=self.browser, url=self.browser.current_url) Способ перехода между страницами.
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Ссылка для входа не появилась."

