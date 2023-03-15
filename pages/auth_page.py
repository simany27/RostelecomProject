from pages.base_page import BasePage
from pages.locators import AuthLocators


class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = "https://b2c.passport.rt.ru/account_b2c/page"
        driver.get(url)
        # создаем нужные элементы
        self.tab_phone = driver.find_element(*AuthLocators.TAB_PHONE)
        self.tab_mail = driver.find_element(*AuthLocators.TAB_MAIL)
        self.tab_login = driver.find_element(*AuthLocators.TAB_LOGIN)
        self.login = driver.find_element(*AuthLocators.AUTH_LOGIN)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.register = driver.find_element(*AuthLocators.REGISTER)

    def enter_phone(self, value):
        self.tab_phone.click()
        self.login.send_keys(value)

    def enter_email(self, value):
        self.tab_mail.click()
        self.login.send_keys(value)

    def enter_pass(self, value):
        self.password.send_keys(value)

    def navigate_to_registration(self):
        self.register.click()

    def btn_click(self):
        self.btn.click()
