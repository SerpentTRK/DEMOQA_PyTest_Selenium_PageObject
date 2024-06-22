
import time

from Pages.Elenents.text_box import ElementsTextBox
from Pages.Elenents.check_box import ElementsCheckBox
from Pages.Elenents.radio_button import ElementsRadioButton
from Pages.Elenents.web_tables import ElementsWebTables
from Pages.Elenents.buttons import Buttons
from Pages.Elenents.links import Links
from Pages.Elenents.broken_links_and_images import BrokenLinksImages
from Pages.Elenents.upload_and_download import UploadAndDownload
from Pages.Form.practice_form import PracticeFormMethods



def test_filling_elements_text_box(browser):
    """
    Заполняем форму Elements/Text Box и сверяем соответствие сохраненных на странице данных с введенными нами
    URL: https://demoqa.com/text-box
    """
    page = ElementsTextBox(browser)
    page.text_box()
    page.data_validation()

def test_filling_elements_check_box_and_validation_data(browser):
    """
    Заполняем форму Elements/Check Box и сверяем соответствие сохраненных на странице данных с введенными нами
    URL: https://demoqa.com/checkbox
    """
    page = ElementsCheckBox(browser)
    page.check_box()
    page.data_validation()

def test_filling_elements_radio_button_and_validation_data(browser):
    """
    Заполняем форму Elements/Radio Button и сверяем соответствие сохраненных на странице данных с введенными нами
    URL: https://demoqa.com/radio-button
    """
    page = ElementsRadioButton(browser)
    page.radio_button()
    page.data_validation()

def test_filling_elements_web_tables_and_validation_data(browser):
    """
    Заполняем форму Forms/Web Tables. Проверяем корректность введенных данных. Удаляем тестовые данные
    URL = https://demoqa.com/webtables
    """
    page = ElementsWebTables(browser)
    page.web_tables()
    page.data_validation()
    page.clier_test_data()

def test_filling_elements_buttons(browser):
    """
    Кликаем на Forms/Buttons. Проверяем нажатие на кнопки
    URL = https://demoqa.com/buttons
    """
    page = Buttons(browser)
    page.buttons()
    page.data_validation()

    time.sleep(3)

def test_filling_elements_links(browser):
    """
    Кликаем на Forms/Links. 1) Переходим по ссылкам 2) Смотрим статус страниц, который нам возвращается
    URL = https://demoqa.com/links

    Тест не обрывается, когда мы получаем статус страницы, отличный от 201, т.к. по смыслу этого тренажера это не требуется
    """
    page = Links(browser)
    page.following_links_will_open_new_tab()
    page.following_links_will_send_an_api_call()

def test_filling_elements_broken_links_and_images(browser):
    """
    Битые ссылки и картинки
    URL = https://demoqa.com/broken
    """
    page = BrokenLinksImages(browser)
    page.image_validation()
    page.links_validation()

def test_upload_and_download(browser):
    page = UploadAndDownload(browser)
    page.download_and_upload_file()
    page.download_and_upload_validation()

def test_filling_forms_practice_form_and_validation_data(browser):
    """
    Заполняем форму Forms/Practice Form и сверяем соответствие сохраненных на странице данных с введенными нами
    URL: https://demoqa.com/automation-practice-form
    """
    page = PracticeFormMethods(browser)
    page.filling_full_form()
    page.data_validation()

def test_temp():
    import requests
    import os

    from selenium import webdriver
    from selenium.webdriver.common.by import By

    # Замените путь к драйверу на путь к вашему драйверу
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/upload-download")

    # Находим кнопку для загрузки файла и загружаем файл
    upload_button = driver.find_element(By.CSS_SELECTOR, "#uploadFile")

    current_dir = os.getcwd()  # Получаем текущий рабочий каталог
    file_path = os.path.join(current_dir, "resources", "1518.jpg")

    upload_button.send_keys(file_path)

    # Подождем некоторое время после загрузки файла
    time.sleep(5)

    # Закрываем браузер
    driver.quit()

















# def test_filling_forms_practice_form_and_validation_data_single_methods(browser):
#     """
#     Это надо убрать из проекта... лишняя детализация
#
#     Заполняем форму Forms/Practice Form и сверяем соответствие сохраненных на странице данных с введенными нами
#     Каждый элемент интерфейса тестируется отдельным методом для данного типа элемента интерфейса
#     URL: https://demoqa.com/automation-practice-form
#     """
#     page = PracticeFormMethods(browser)
#     page.filling_full_form_single_methods()  # заполнение формы
#     page.data_validation_single()    # сверка вводимых и сохраненных данных

# # не работает, т.к. тут не работает selene
# def test_page_object():
#     from selene.api import *
#
#     # from selene import browser, by, be, have
#     # from selene.support.shared.jquery_style import s, ss
#     from selenium.webdriver import ActionChains, Keys
#
#     browser.open('https://demoqa.com/automation-practice-form')
#
#     class RegistrationPage:
#         def fill_form(self, anchor, data):
#             # Заполнить поля First Name и Last Name
#             anchors_for_names = anchor[0].split()
#             first_last_name = data[0].split()
#
#             browser.element(anchors_for_names[0]).type(first_last_name[0]);
#             browser.element(anchors_for_names[1]).type(first_last_name[1])
#
#             # Заполняем поле email
#             browser.element(anchor[1]).type(data[1])
#
#             # Выбрать пол Gender
#             browser.element(anchor[2]).click()
#
#             # Заполнить поле Mobile Number
#             browser.element(anchor[3]).type(data[3])
#
#             # Заполнить дату рождения
#             field_date_of_birth = browser.element(anchor[4])
#             for _ in range(10):
#                 field_date_of_birth.send_keys(Keys.BACKSPACE)
#             field_date_of_birth.type(data[4]).press_escape()
#
#             # Выбрать предмет
#             browser.element(anchor[5]).type(data[5]).press_enter()
#
#             # Выбрать хобби
#             browser.element(anchor[6]).click()
#
#             # Загрузить фотографию
#             photo_input = browser.element(anchor[7])
#             photo_path = "E:\\вандрайв\\ПРЯЖА\\Библиотека картинок\\Льняная и хлопковая пряжа\\ЛЬНЯНАЯ\\" + data[7]
#             photo_input.send_keys(photo_path)
#
#             # Заполнить адрес
#             browser.element(anchor[8]).type(data[8])
#
#             # Прокрутить страницу ниже на 200 пикселей:
#             s("body").send_keys(Keys.ARROW_DOWN * 4)
#
#             # Выбрать штат и город
#             anchor_for_state_sity = anchor[9].split()
#             state_sity = data[9].split()
#
#             browser.element(anchor_for_state_sity[0]).click()
#             browser.element('//div[text()="{}"]'.format(state_sity[0])).click()
#             browser.element(anchor_for_state_sity[1]).click()
#             browser.element('//div[@id="city"]//div[contains(text(), "{}")]'.format(state_sity[1])).click()
#
#         def submit_form(self):
#             # Нажать кнопку Submit
#             browser.element('.text-right.col-md-2.col-sm-12 #submit').click()
#
#         def verify_data(self, data):
#             # Проверить сохраненные данные на соответствие
#             for item in data:
#                 browser.element(by.text(item)).should(be.visible)
#
#         def close_modal(self):
#             # Закрыть модальное окно
#             browser.element('#closeLargeModal').click()
#
#     # по идее эти данные, anchors и data_for_registranion, если они будут использоваться в разных тестах, мы уносим
#     # в сторону, и в разных тестах их принимаем. Можно сделать генератор случайных данных..
#
#     anchors = ['#firstName #lastName',
#                 '.col-md-9.col-sm-12 #userEmail',
#                 '[for="gender-radio-1"]',
#                 '.col-md-9.col-sm-12 #userNumber',
#                 '#dateOfBirthInput',
#                '#subjectsInput',
#                '//label[@for="hobbies-checkbox-1"]',
#                '#uploadPicture',
#                '#currentAddress',
#                '#state #city']
#
#     data_for_registranion = ['Василий Алибабаевич',
#                              'vasya@test.ru',
#                              'Male',
#                              '4951112233',
#                              '01 January,2000',
#                              'Maths',
#                              'Sports',
#                              '1800.jpg',
#                              'А/Я 000002, на деревню Дедушке',
#                              'Rajasthan Jaipur']
#
#     registration_page = RegistrationPage()
#     registration_page.fill_form(anchors, data_for_registranion)
#     registration_page.submit_form()
#     registration_page.verify_data(data_for_registranion)
#     registration_page.close_modal()



