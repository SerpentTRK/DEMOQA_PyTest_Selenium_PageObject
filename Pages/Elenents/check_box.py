from selenium.webdriver.common.by import By

from Data_for_tests.Elements.check_box_testdata import Url, ChrckBoxLocators, CheckBoxTestdata
from Methods.methods import Methods

class ElementsCheckBox(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def check_box(self):
        # раскрываем меню чекбоксов
        self.find_element(ChrckBoxLocators.LOCATOR_EXPAND_ALL).click()
        # кликаем на одиночном элементе
        self.find_element(ChrckBoxLocators.LOCATOR_NOTES).click()
        # кликаем на папке
        self.find_element(ChrckBoxLocators.LOCATOR_WORKSPACE).click()
        # одиночный элемент
        self.find_element(ChrckBoxLocators.LOCATOR_GENEGAL).click()

    def data_validation(self):
        res = []
        elements = self.find_elements((By.CSS_SELECTOR, ".display-result.mt-4"))
        for element in elements:
            # text_elem = element.text.split(":")[-1].strip() #дилим строку по разделителю, и удаляем все пробелы
            res.append(element.text)
        # res = ['You have selected :\nnotes\nworkspace\nreact\nangular\nveu\ngeneral']
        # Извлекаем строки, разделенные символом новой строки, за исключением первой строки
        result = res[0].split('\n')[1:]

        assert CheckBoxTestdata.DATA_NOTES in result
        assert CheckBoxTestdata.DATA_WORKSPACE in result
        assert CheckBoxTestdata.DATA_REACT in result
        assert CheckBoxTestdata.DATA_ANGULAR in result
        assert CheckBoxTestdata.DATA_VEU in result
        assert CheckBoxTestdata.DATA_GENERAL in result


