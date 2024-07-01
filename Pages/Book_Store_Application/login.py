
import time

from selenium.webdriver import ActionChains

from Data_for_tests.Book_Store_Application.login_testdata import Url, LoginLocators, LoginTestdata
from Methods.methods import Methods

class Login(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def use_login_page(self):
        # self.new_user_authorization()
        # self.new_user_registration()  # они туда "капчу" с картинкой засунули..
        self.new_user_authorization()
        # self.delete_accaunt()

    def new_user_authorization(self):
        self.find_element(LoginLocators.LOCATOR_USER_NAME).send_keys(LoginTestdata.DATA_UserName)
        self.find_element(LoginLocators.LOCATOR_PASSWORD).send_keys(LoginTestdata.DATA_Password)
        self.find_element(LoginLocators.LOCATOR_LOGIN_BUTTON).click()

        # fail_authorizatoion = self.find_element(LoginLocators.LOCATOR_FAIL_AUTHORIZATION)
        # assert fail_authorizatoion.text == LoginTestdata.DATA_fail_authorizatoion

    def new_user_registration(self):
        self.find_element(LoginLocators.LOCATOR_NEW_USER_BUTTON).click()

        self.find_element(LoginLocators.LOCATOR_REGISTRATION_First_Name).send_keys(LoginTestdata.DATA_FIRS_NAME)
        time.sleep(1)
        self.find_element(LoginLocators.LOCATOR_REGISTRATION_Last_Name).send_keys(LoginTestdata.DATA_LAST_NAME)
        time.sleep(1)
        self.find_element(LoginLocators.LOCATOR_USER_NAME).send_keys(LoginTestdata.DATA_UserName)
        time.sleep(1)
        self.find_element(LoginLocators.LOCATOR_PASSWORD).send_keys(LoginTestdata.DATA_Password)
        time.sleep(1)

        iframe_captcha = self.find_element(LoginLocators.LOCATOR_REGISTRATION_iFrame_CAPtCHA)
        self.browser.switch_to.frame(iframe_captcha)
        captcha = self.find_element(LoginLocators.LOCATOR_REGISTRATION_CAPTCHA)
        ActionChains(self.browser).double_click(captcha).perform()
        time.sleep(5)
        self.browser.switch_to.default_content()

        self.find_element(LoginLocators.LOCATOR_REGISTRATION_Register_BUTTON).click()
        time.sleep(1)

        alert = self.browser.switch_to.alert
        alert.accept()
        time.sleep(1)

        self.find_element(LoginLocators.LOCATOR_REGISTRATION_Back_to_Login_BUTTON).click()

    def delete_accaunt(self):
        self.find_element(LoginLocators.LOCATOR_DELETE_ACCAUNT).click()
        self.find_element(LoginLocators.LOCATOR_DELETE_ACCAUNT).click()


        # self.find_element(LoginLocators.LOCATOR_DELETE_ACCAUNT_ALERT).click()
        alert = self.browser.switch_to.alert
        print(f"Текст на странице ALERT: {alert.text}")
        alert.accept()

