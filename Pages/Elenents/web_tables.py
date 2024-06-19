from selenium.webdriver.common.by import By

from Data_for_tests.Elements.web_tables_testdata import Url, WebTablesLocators, WebTablesTestdata
from Data_for_tests.Form.practice_form_testdata import PracticeFormTestdata
from Methods.methods import Methods

class ElementsWebTables(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def web_tables(self):
        self.find_element(WebTablesLocators.LOCATOR_BUTTON_ADD).click()
        self.find_element(WebTablesLocators.LOCATOR_FIRST_NAME).send_keys(PracticeFormTestdata.DATA_FIRST_NAME)
        self.find_element(WebTablesLocators.LOCATOR_LAST_NAME).send_keys(PracticeFormTestdata.DATA_LAST_NAME)
        self.find_element(WebTablesLocators.LOCATOR_EMAIL_FIELD).send_keys(PracticeFormTestdata.DATA_EMAIL_FIELD)
        self.find_element(WebTablesLocators.LOCATOR_AGE).send_keys(WebTablesTestdata.DATA_AGE)
        self.find_element(WebTablesLocators.LOCATOR_SALARY).send_keys(WebTablesTestdata.DATA_SALARY)
        self.find_element(WebTablesLocators.LOCATOR_DEPARTMENT).send_keys(WebTablesTestdata.DATA_DEPARTMENT)
        self.find_element(WebTablesLocators.LOCATOR_BUTTON_SUBMIT).click()

