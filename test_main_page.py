from selenium.webdriver.common.by import By
import time
link = " http://selenium1py.pythonanywhere.com"

def test_guest_should_see_basket_form(browser):
    browser.get(link)
    time.sleep(3)
    button = browser.find_element(By.XPATH, "//*[@id='login_link']")
    assert button, "Кнопка не найдена"