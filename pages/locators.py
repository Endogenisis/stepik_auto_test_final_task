from selenium.webdriver.common.by import By

# Файл локаторов для поверок.
class MainPageLocators():
    LOGIN_LINK = (By.XPATH, '//*[@id="login_link"]')

class LoginPageLocators():
    Login_form = (By.ID, "login_form")
    Register_form = (By.ID, "register_form")

class ProductPageLocators():
    Add_cart = (By.ID, "add_to_basket_form")
    Add_cart_assert = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    product_name = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    cart_price = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    price_product = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    SUCCESS_MESSAGE = (By.XPATH, '// *[ @ id = "messages"] / div[1] / div')

class BasePageLocators():
    LOGIN_LINK = (By.XPATH, '//*[@id="login_link"]')
    LOGIN_LINK_INVALID = (By.XPATH, '//*[@id="login_link_inc"]')
class BasketPageLocators():
    basket_link = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    empty_basket = (By.XPATH, '//*[@id="content_inner"]/p')
    not_empty_basket = (By.XPATH, '//*[@id="content_inner"]/div[1]/div/h2')

