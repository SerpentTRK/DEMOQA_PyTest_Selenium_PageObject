import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/webtables"

class WebTablesLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_BUTTON_ADD = (By.CSS_SELECTOR, "#addNewRecordButton")
    LOCATOR_FIRST_NAME = (By.CSS_SELECTOR, "#firstName-wrapper #firstName")
    LOCATOR_LAST_NAME = (By.CSS_SELECTOR, "#lastName-wrapper #lastName")
    LOCATOR_EMAIL_FIELD = (By.CSS_SELECTOR, "#userEmail-wrapper #userEmail")
    LOCATOR_AGE = (By.CSS_SELECTOR, "#age-wrapper #age")
    LOCATOR_SALARY = (By.CSS_SELECTOR, "#salary-wrapper #salary")
    LOCATOR_DEPARTMENT = (By.CSS_SELECTOR, "#department-wrapper #department")
    LOCATOR_BUTTON_SUBMIT = (By.ID, "submit")
    LOCATOR_SEARCHBOX = (By.ID, "searchBox")
    LOCATOR_RECORD_EDIT = (By.CSS_SELECTOR, ".mr-2")
    LOCATOR_ELEMENTS = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div")
    LOCATOR_DELETE = (By.ID, "delete-record-4")


class WebTablesTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_AGE = ["36", "46"]
    DATA_SALARY = "300000"
    DATA_DEPARTMENT = "IT"
