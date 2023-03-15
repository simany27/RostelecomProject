from selenium.webdriver.common.by import By


class AuthLocators:
    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_MAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    AUTH_LOGIN = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")
    REGISTER = (By.ID, "kc-register")

class RegisterLocators:
    FIRSTNAME = (By.CSS_SELECTOR, "input[name='firstName']")
    LASTNAME = (By.CSS_SELECTOR, "input[name='lastName']")
    ADDRESS = (By.CSS_SELECTOR, "input[id='address']")
    PASSWORD = (By.CSS_SELECTOR, "input[id='password']")
    PASSWORD_CONF = (By.CSS_SELECTOR, "input[id='password-confirm']")
    REG_BTN = (By.CSS_SELECTOR, "button[name='register']")