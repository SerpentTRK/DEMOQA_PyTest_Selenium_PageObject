import time

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
        # заводим новую запись
        self.find_element(WebTablesLocators.LOCATOR_BUTTON_ADD).click()
        self.find_element(WebTablesLocators.LOCATOR_FIRST_NAME).send_keys(PracticeFormTestdata.DATA_FIRST_NAME)
        self.find_element(WebTablesLocators.LOCATOR_LAST_NAME).send_keys(PracticeFormTestdata.DATA_LAST_NAME)
        self.find_element(WebTablesLocators.LOCATOR_EMAIL_FIELD).send_keys(PracticeFormTestdata.DATA_EMAIL_FIELD)
        self.find_element(WebTablesLocators.LOCATOR_AGE).send_keys(WebTablesTestdata.DATA_AGE[0])
        self.find_element(WebTablesLocators.LOCATOR_SALARY).send_keys(WebTablesTestdata.DATA_SALARY)
        self.find_element(WebTablesLocators.LOCATOR_DEPARTMENT).send_keys(WebTablesTestdata.DATA_DEPARTMENT)
        self.find_element(WebTablesLocators.LOCATOR_BUTTON_SUBMIT).click()
        # Редактирование нашей записи. Разбивается на несколько этапов, т.к. нам надо универсально находить нашу запись
        # при любом количестве записей в таблице. За одно проверяем элементы интерфейса
        # поиск нашей записи
        self.find_element(WebTablesLocators.LOCATOR_SEARCHBOX).send_keys(PracticeFormTestdata.DATA_EMAIL_FIELD)
        # редактирование нашей записи
        self.find_element(WebTablesLocators.LOCATOR_RECORD_EDIT).click()
        self.find_element(WebTablesLocators.LOCATOR_AGE).clear()
        self.find_element(WebTablesLocators.LOCATOR_AGE).send_keys(WebTablesTestdata.DATA_AGE[1])
        self.find_element(WebTablesLocators.LOCATOR_BUTTON_SUBMIT).click()

    def data_validation(self):
        elements = self.find_elements(WebTablesLocators.LOCATOR_ELEMENTS)
        res = []
        for element in elements:
            res.append(element.text)
        result = res[0].split('\n')  # ['Василий', 'Алибабаевич', '46', 'vasya@test.ru', '300000', 'IT']

        assert PracticeFormTestdata.DATA_FIRST_NAME in result, f"Ошибка: First Name {PracticeFormTestdata.DATA_FIRST_NAME} не найдено в результатах поиска"
        assert PracticeFormTestdata.DATA_LAST_NAME in result, f"Ошибка: Last Name {PracticeFormTestdata.DATA_LAST_NAME} не найдена в результатах поиска"
        assert WebTablesTestdata.DATA_AGE[-1] in result, f"Ошибка: Age {WebTablesTestdata.DATA_AGE[-1]} не найден в результатах поиска"
        assert PracticeFormTestdata.DATA_EMAIL_FIELD in result, f"Ошибка: Email {PracticeFormTestdata.DATA_EMAIL_FIELD} не найден в результатах поиска"
        assert WebTablesTestdata.DATA_SALARY in result, f"Ошибка: Salary {WebTablesTestdata.DATA_SALARY} не найдена в результатах поиска"
        assert WebTablesTestdata.DATA_DEPARTMENT in result, f"Ошибка: Depatment {WebTablesTestdata.DATA_DEPARTMENT} не найден в результатах поиска"

    def clier_test_data(self):
        self.find_element(WebTablesLocators.LOCATOR_DELETE).click()
        # self.find_element(WebTablesLocators.LOCATOR_SEARCHBOX).clear() # я не понимаю почему, но не срабатывает.
        # Если руками очистить поле, то видны дефолтные записи, а нашей нет. Она удалена.
