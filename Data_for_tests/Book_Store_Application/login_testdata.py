import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/login"

class LoginLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_USER_NAME = (By.CSS_SELECTOR, "#userName")
    LOCATOR_PASSWORD = (By.CSS_SELECTOR, "#password")
    LOCATOR_LOGIN_BUTTON = (By.CSS_SELECTOR, "#login")
    LOCATOR_NEW_USER_BUTTON = (By.CSS_SELECTOR, "#newUser")

    LOCATOR_FAIL_AUTHORIZATION = (By.CSS_SELECTOR, "#name")

    LOCATOR_REGISTRATION_First_Name = (By.CSS_SELECTOR, "#firstname")
    LOCATOR_REGISTRATION_Last_Name = (By.CSS_SELECTOR, "#lastname")
    # LOCATOR_REGISTRATION_UserName = LOCATOR_USER_NAME
    # LOCATOR_REGISTRATION_Password = LOCATOR_PASSWORD
    LOCATOR_REGISTRATION_iFrame_CAPtCHA = (By.CSS_SELECTOR, "#g-recaptcha > div > div > iframe")
    LOCATOR_REGISTRATION_CAPTCHA = (By.CSS_SELECTOR, "#recaptcha-anchor-label")
    LOCATOR_REGISTRATION_Back_to_Login_BUTTON = (By.CSS_SELECTOR, "#gotologin")
    LOCATOR_REGISTRATION_Register_BUTTON = (By.CSS_SELECTOR, "#register")

    LOCATOR_DELETE_ACCAUNT = (By.CSS_SELECTOR, "#submit:nth-of-type(2)")
    LOCATOR_DELETE_ACCAUNT_ASSEPT = (By.CSS_SELECTOR, "#closeSmallModal-ok")
    LOCATOR_DELETE_ACCAUNT_ALERT = (By.CSS_SELECTOR, "")

class LoginTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_UserName = "SlonDuDu"
    DATA_Password = "qPortnsE.18$"
    DATA_fail_authorizatoion = "Invalid username or password!"
    DATA_FIRS_NAME = "Вениамин"
    DATA_LAST_NAME = "Пипеткин"