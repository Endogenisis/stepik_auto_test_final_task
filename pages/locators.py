from selenium.webdriver.common.by import By

# Файл лкаторов для поверок.
class MainPageLocators():
    LOGIN_LINK = (By.XPATH, '//*[@id="login_link"]')

class LoginPageLocators():
    Login_form = (By.ID, "login_form")
    Register_form = (By.ID, "register_form")