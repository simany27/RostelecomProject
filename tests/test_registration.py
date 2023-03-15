import time

import pytest
from selenium.webdriver.common.by import By

from pages.auth_page import AuthPage
from pages.locators import RegisterLocators
from settings import valid_firstname, valid_lastname, valid_password, valid_em_reg, valid_phone_reg

def test_registration_page_with_valid_mail(web_browser):
    page = AuthPage(web_browser)
    page.navigate_to_registration()
    web_browser.find_element(*RegisterLocators.FIRSTNAME).send_keys(valid_firstname)
    web_browser.find_element(*RegisterLocators.LASTNAME).send_keys(valid_lastname)
    web_browser.find_element(*RegisterLocators.ADDRESS).send_keys(valid_em_reg)
    web_browser.find_element(*RegisterLocators.PASSWORD).send_keys(valid_password)
    web_browser.find_element(*RegisterLocators.PASSWORD_CONF).send_keys(valid_password)
    web_browser.find_element(*RegisterLocators.REG_BTN).click()
    assert web_browser.find_element(By.XPATH, "//h1[contains(text(), 'Подтверждение email')]"), "registration error"

def test_registration_page_with_valid_phone(web_browser):
    page = AuthPage(web_browser)
    page.navigate_to_registration()
    web_browser.find_element(*RegisterLocators.FIRSTNAME).send_keys(valid_firstname)
    web_browser.find_element(*RegisterLocators.LASTNAME).send_keys(valid_lastname)
    web_browser.find_element(*RegisterLocators.ADDRESS).send_keys(valid_phone_reg)
    web_browser.find_element(*RegisterLocators.PASSWORD).send_keys(valid_password)
    web_browser.find_element(*RegisterLocators.PASSWORD_CONF).send_keys(valid_password)
    web_browser.find_element(*RegisterLocators.REG_BTN).click()
    assert web_browser.find_element(By.XPATH, "//h1[contains(text(), 'Подтверждение телефона')]"), "registration error"

@pytest.mark.parametrize("firstname", ["А", "SD", "-/*"], ids=["1 символ", "Не кириллица", "СпецСимволы"])
@pytest.mark.parametrize("lastname", ["А", "SD", "-/*"], ids=["1 символ", "Не кириллица", "СпецСимволы"])
@pytest.mark.parametrize("email_or_phone", ["fdfghjhmail.ru", "hjkfdoe@@mail.ru", "jkhkfhak@", "5555", "00000000000"],
                         ids=["email без @", "Два @", "Пусто после @", "Короткий номер", "Номер из нулей"])
def test_registration_page_with_invalid_data(web_browser, firstname, lastname, email_or_phone):
    page = AuthPage(web_browser)
    page.navigate_to_registration()
    web_browser.find_element(*RegisterLocators.FIRSTNAME).send_keys(firstname)
    web_browser.find_element(*RegisterLocators.LASTNAME).send_keys(lastname)
    web_browser.find_element(*RegisterLocators.ADDRESS).send_keys(email_or_phone)
    web_browser.find_element(*RegisterLocators.PASSWORD).send_keys(valid_password)
    web_browser.find_element(*RegisterLocators.PASSWORD_CONF).send_keys(valid_password)
    web_browser.find_element(*RegisterLocators.REG_BTN).click()
    assert web_browser.find_element(By.CSS_SELECTOR, "span[class='rt-input-container__meta rt-input-container__meta--error']"), "registration error"

