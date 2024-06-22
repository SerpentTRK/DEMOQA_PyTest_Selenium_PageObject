from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Data_for_tests.Form.practice_form_testdata import Url, PracticeFormLocators, PracticeFormTestdata
from Methods.methods import Methods


class PracticeFormMethods(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # наверное тут его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def filling_full_form(self):
        # text box
        self.find_element(PracticeFormLocators.LOCATOR_FIRST_NAME).send_keys(PracticeFormTestdata.DATA_FIRST_NAME)
        # text box
        self.find_element(PracticeFormLocators.LOCATOR_LAST_NAME).send_keys(PracticeFormTestdata.DATA_LAST_NAME)
        # text box
        self.find_element(PracticeFormLocators.LOCATOR_EMAIL_FIELD).send_keys(PracticeFormTestdata.DATA_EMAIL_FIELD)
        # radio button
        self.find_element(PracticeFormLocators.LOCATOR_GENDER).click()
        # text box
        self.find_element(PracticeFormLocators.LOCATOR_MOBILE_NUMBER).send_keys(PracticeFormTestdata.DATA_MOBILE_NUMBER)
        # data-picker
        self.find_element(PracticeFormLocators.LOCATOR_DATE_OF_BIRTH).click()
        Select(self.find_element(PracticeFormLocators.LOCATOR_DATE_OF_BIRTH_YEAR))\
                                                .select_by_visible_text(PracticeFormTestdata.DATA_DATE_OF_BIRTH_YEAR)
        Select(self.find_element(PracticeFormLocators.LOCATOR_DATE_OF_BIRTH_MONTH))\
                                                .select_by_visible_text(PracticeFormTestdata.DATA_DATE_OF_BIRTH_MONTH)
        self.find_element(PracticeFormLocators.LOCATOR_DATE_OF_BIRTH_DAY).click()
        # widget Auto Complete
        subject = self.find_element(PracticeFormLocators.LOCATOR_SUBJECTS)
        subject.send_keys(PracticeFormTestdata.DATA_SUBJECTS)
        subject.send_keys(Keys.RETURN)
        # checkbox
        self.find_element(PracticeFormLocators.LOCATOR_HOBBIES).click()
        # Upload and Download
        self.find_element(PracticeFormLocators.LOCATOR_PICTURE).send_keys(PracticeFormTestdata.DATA_PICTURE)
        # text box
        self.find_element(PracticeFormLocators.LOCATOR_CURRENT_ADDRESS).send_keys(PracticeFormTestdata.DATA_CURRENT_ADDRESS)
        # Скроллинг страницы
        self.scroll_down_page(200)
        # виджет Select Menu
        self.find_element(PracticeFormLocators.LOCATOR_STATE).click()
        self.find_element(PracticeFormLocators.LOCATOR_STATE_NAME).click()
        # виджет Select Menu
        self.find_element(PracticeFormLocators.LOCATOR_CITY).click()
        self.find_element(PracticeFormLocators.LOCATOR_CITY_NAME).click()
        # button
        self.find_element(PracticeFormLocators.LOCATOR_BUTTON_SUBMIT).click()

    def data_validation(self):
        assert self.find_element(PracticeFormLocators.LOCATOR_DATA_FULL_NAME_VALIDATION).text == \
               PracticeFormTestdata.DATA_FULL_NAME, f"Ошибка: {PracticeFormTestdata.DATA_FULL_NAME} не обнаружено"

        assert self.find_element(PracticeFormLocators.LOCATOR_DATA_EMAIL_FIELD_VALIDATOIN).text == \
               PracticeFormTestdata.DATA_EMAIL_FIELD, f"Ошибка: {PracticeFormTestdata.DATA_EMAIL_FIELD} не обнаружено"

        assert self.find_element(PracticeFormLocators.LOCATOR_DATA_GENDER_VALIDATION).text == \
               PracticeFormTestdata.DATA_GENDER, f"Ошибка: {PracticeFormTestdata.DATA_GENDER} не обнаружено"

        assert self.find_element(PracticeFormLocators.LOCATOR_DATA_MOBILE_NUMBER_VALIDATION).text == \
               PracticeFormTestdata.DATA_MOBILE_NUMBER, f"Ошибка: {PracticeFormTestdata.DATA_MOBILE_NUMBER} не обнаружено"

        assert self.find_element(PracticeFormLocators.LOCATOR_DATA_DATE_OF_BIRTH_VALIDATION).text == \
               PracticeFormTestdata.DATA_DATE_OF_BIRTH, f"Ошибка: {PracticeFormTestdata.DATA_DATE_OF_BIRTH} не обнаружено"

        assert self.find_element(PracticeFormLocators.LOCATOR_DATA_SUBJECTS_VALIDATION).text == \
               PracticeFormTestdata.DATA_SUBJECTS, f"Ошибка: {PracticeFormTestdata.DATA_SUBJECTS} не обнаружено"

        assert self.find_element(PracticeFormLocators.LOCATOR_DATA_HOBBIES_VALIDATION).text == \
               PracticeFormTestdata.DATA_HOBBIES, f"Ошибка: {PracticeFormTestdata.DATA_HOBBIES} не обнаружено"

        assert self.find_element(PracticeFormLocators.LOCATOR_DATA_PICTURE_FILENAME_VALIDATION).text == \
               PracticeFormTestdata.DATA_PICTURE_FILENAME, f"Ошибка: {PracticeFormTestdata.DATA_PICTURE_FILENAME} не обнаружено"

        assert self.find_element(PracticeFormLocators.LOCATOR_DATA_CURRENT_ADDRESS_VALIDATION).text == \
               PracticeFormTestdata.DATA_CURRENT_ADDRESS, f"Ошибка: {PracticeFormTestdata.DATA_CURRENT_ADDRESS} не обнаружено"

        assert self.find_element(PracticeFormLocators.LOCATOR_DATA_STATE_CITY_VALIDATION).text == \
               PracticeFormTestdata.DATA_STATE_CITY, f"Ошибка: {PracticeFormTestdata.DATA_STATE_CITY} не обнаружено"

    # def filling_full_form_single_methods(self):
    #     self.text_box(PracticeFormLocators.LOCATOR_FIRST_NAME, PracticeFormTestdata.DATA_FIRST_NAME)
    #     self.text_box(PracticeFormLocators.LOCATOR_LAST_NAME, PracticeFormTestdata.DATA_LAST_NAME)
    #     self.text_box(PracticeFormLocators.LOCATOR_EMAIL_FIELD, PracticeFormTestdata.DATA_EMAIL_FIELD)
    #     self.radio_button(PracticeFormLocators.LOCATOR_GENDER)
    #     self.text_box(PracticeFormLocators.LOCATOR_MOBILE_NUMBER, PracticeFormTestdata.DATA_MOBILE_NUMBER)
    #     self.data_picker(PracticeFormLocators.LOCATOR_DATE_OF_BIRTH,
    #                      PracticeFormLocators.LOCATOR_DATE_OF_BIRTH_YEAR,
    #                      PracticeFormTestdata.DATA_DATE_OF_BIRTH_YEAR,
    #                      PracticeFormLocators.LOCATOR_DATE_OF_BIRTH_MONTH,
    #                      PracticeFormTestdata.DATA_DATE_OF_BIRTH_MONTH,
    #                      PracticeFormLocators.LOCATOR_DATE_OF_BIRTH_DAY)
    #     self.widget_auto_complite(PracticeFormLocators.LOCATOR_SUBJECTS, PracticeFormTestdata.DATA_SUBJECTS)
    #     self.checkbox(PracticeFormLocators.LOCATOR_HOBBIES)
    #     self.upload_and_download(PracticeFormLocators.LOCATOR_PICTURE, PracticeFormTestdata.DATA_PICTURE)
    #     self.text_box(PracticeFormLocators.LOCATOR_CURRENT_ADDRESS, PracticeFormTestdata.DATA_CURRENT_ADDRESS)
    #     self.scroll_down_page(200)
    #     self.widget_select_menu_one(PracticeFormLocators.LOCATOR_STATE, PracticeFormLocators.LOCATOR_STATE_NAME)
    #     self.widget_select_menu_one(PracticeFormLocators.LOCATOR_CITY, PracticeFormLocators.LOCATOR_CITY_NAME)
    #     self.button(PracticeFormLocators.LOCATOR_BUTTON_SUBMIT)
    #
    # def data_validation_single(self):
    #     assert self.browser.find_element(By.CSS_SELECTOR, "table tbody tr:nth-child(1) td:nth-child(2)")\
    #                .text == PracticeFormTestdata.DATA_FULL_NAME
    #     assert self.browser.find_element(By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(2) td:nth-child(2)")\
    #                .text == PracticeFormTestdata.DATA_EMAIL_FIELD
    #     assert self.browser.find_element(By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(3) td:nth-child(2)")\
    #                .text == PracticeFormTestdata.DATA_GENDER
    #     assert self.browser.find_element(By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(4) td:nth-child(2)")\
    #                .text == PracticeFormTestdata.DATA_MOBILE_NUMBER
    #     assert self.browser.find_element(By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(5) td:nth-child(2)")\
    #                .text == PracticeFormTestdata.DATA_DATE_OF_BIRTH
    #     assert self.browser.find_element(By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(6) td:nth-child(2)") \
    #                .text == PracticeFormTestdata.DATA_SUBJECTS
    #     assert self.browser.find_element(By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(7) td:nth-child(2)") \
    #                .text == PracticeFormTestdata.DATA_HOBBIES
    #     assert self.browser.find_element(By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(8) td:nth-child(2)") \
    #                .text == PracticeFormTestdata.DATA_PICTURE_FILENAME
    #     assert self.browser.find_element(By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(9) td:nth-child(2)") \
    #                .text == PracticeFormTestdata.DATA_CURRENT_ADDRESS
    #     assert self.browser.find_element(By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(10) td:nth-child(2)") \
    #                .text == PracticeFormTestdata.DATA_STATE_CITY



        # result_page.should_have_text(test_data['first_name']) \
        #     .should_have_text(test_data['last_name']) \
        #     .should_have_text(test_data['email']) \
        #     .should_have_text(test_data['gender']) \
        #     .should_have_text(test_data['mobile']) \
        #     .should_have_text(test_data['date_of_birth']['day']) \
        #     .should_have_text(test_data['date_of_birth']['month']) \
        #     .should_have_text(test_data['date_of_birth']['year']) \
        #     .should_have_text(test_data['subjects'][0]) \
        #     .should_have_hobbies(test_data['hobbies']) \
        #     .should_have_text(test_data['current_address']) \
        #     .should_have_text(test_data['state']) \
        #     .should_have_text(test_data['city']) \
        #     .close()