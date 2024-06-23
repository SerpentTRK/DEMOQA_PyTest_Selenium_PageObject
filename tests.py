
import time

from Pages.Alerts_Frame_Windows.frames import Frames
from Pages.Alerts_Frame_Windows.alerts import Alerts
from Pages.Alerts_Frame_Windows.browser_windows import BrowserWindows
from Pages.Alerts_Frame_Windows.modal_dialogs import ModalDialogs
from Pages.Alerts_Frame_Windows.nested_frames import NestedFrames

from Pages.Form.practice_form import PracticeFormMethods

from Pages.Elenents.dynamic_properties import DynamicProperties
from Pages.Elenents.upload_and_download import UploadAndDownload
from Pages.Elenents.broken_links_and_images import BrokenLinksImages
from Pages.Elenents.links import Links
from Pages.Elenents.buttons import Buttons
from Pages.Elenents.web_tables import ElementsWebTables
from Pages.Elenents.radio_button import ElementsRadioButton
from Pages.Elenents.check_box import ElementsCheckBox
from Pages.Elenents.text_box import ElementsTextBox



# Раздел "Elements"
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
    """
    Получение и отправка файлов.
    URL = https://demoqa.com/upload-download
    """
    page = UploadAndDownload(browser)
    page.download_and_upload_file()
    page.download_and_upload_validation()

def test_dynamic_properties(browser):
    """
    Динамически появялющиеся элементы (кнопки)
    URL = https://demoqa.com/dynamic-properties
    """
    page = DynamicProperties(browser)
    page.push_dynamic_buttons()

# Раздел "Forms"
def test_filling_forms_practice_form_and_validation_data(browser):
    """
    Заполняем форму Forms/Practice Form и сверяем соответствие сохраненных на странице данных с введенными нами
    URL: https://demoqa.com/automation-practice-form
    """
    page = PracticeFormMethods(browser)
    page.filling_full_form()
    page.data_validation()

# Раздел "Alerts, Frame & Windows"
def test_browser_windows(browser):
    """
    Работа с табами и новыми окнами. Открываем, выводим текст...
    URL: https://demoqa.com/browser-windows
    """
    page = BrowserWindows(browser)
    page.open_new_tabs_and_windows()

def test_alerts(browser):
    """
    Работа с окнами Alerts. Сообщение из первых двух Alert выводится на print.
    Результаты Confirm и Prompt передаем на assert.
    URL: https://demoqa.com/alerts
    """
    page = Alerts(browser)
    page.click_alerts_button()

def test_frames(browser):
    """
    Работа с Frames. Находим, переключаемся, выводим содержимое
    URL: https://demoqa.com/frames
    """
    page = Frames(browser)
    page.iframe_action()

def test_nested_frames(browser):
    """
    Работа с Frames и вложенным в него фреймом. Находим, переключаемся, выводим содержимое
    URL: https://demoqa.com/nestedframes
    """
    page = NestedFrames(browser)
    page.nested_iframe_action()

def test_modal_dialogs(browser):
    """
    Работа с Модальными диалоговыми окнами. Находим, переключаемся, выводим содержимое
    URL: https://demoqa.com/modal-dialogs
    """
    page = ModalDialogs(browser)
    page.modal_dialog_windows()


# Черновик
def test_temp():
    import requests
    import os

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Замените путь к драйверу на путь к вашему драйверу
    driver = webdriver.Chrome()
    # Открываем страницу demoqa.com/browser-windows
    driver.get("https://demoqa.com/browser-windows")

    # Находим кнопку для открытия окна
    wait = WebDriverWait(driver, 10)
    button = driver.find_element(By.CSS_SELECTOR, "button#messageWindowButton")
    button.click()

    # # Переключаемся на новое окно
    # wait.until(EC.number_of_windows_to_be(2))
    #
    # new_window = driver.window_handles[1]
    # driver.switch_to.window(new_window)
    #
    # # # Получаем текст из открывшегося окна
    # # text = driver.find_element(By.CSS_SELECTOR, "body").text
    # # print(text)
    # # Получаем текст из элемента "body" с помощью JavaScript
    # body_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
    # text = driver.execute_script("return arguments[0].innerText;", body_element)
    # print(text)
    #
    # # Закрываем окно
    # driver.close()
    #
    # # Переключаемся обратно на основное окно
    # driver.switch_to.window(driver.window_handles[0])
    #
    # # Закрываем браузер
    # driver.quit()

    # Переключаемся на новое окно
    wait.until(EC.number_of_windows_to_be(2))
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    # Дожидаемся появления элемента iframe в новом окне
    iframe_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe")))

    # Переключаемся в iframe
    driver.switch_to.frame(iframe_element)

    # Дожидаемся появления текста внутри iframe
    text_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p")))

    # Получаем текст из элемента внутри iframe
    text = text_element.text
    print(text)

    # Переключаемся обратно из iframe
    driver.switch_to.default_content()

    # Закрываем окно и браузер
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.quit()






    # # Переключаемся на iframe, если текст находится внутри него
    # iframe = driver.find_element(By.CSS_SELECTOR, "iframe")
    # driver.switch_to.frame(iframe)
    #
    # # Получаем текст из информационного окна
    # info_text = driver.find_element(By.ID, "sampleHeading").text
    # print(info_text)
    #
    # # Переключаемся обратно на основную страницу
    # driver.switch_to.default_content()
    #
    # # Закрываем информационное окно
    # close_button = driver.find_element(By.CSS_SELECTOR, "button#closeSmallModal")
    # close_button.click()
    #
    # # Закрываем браузер
    # driver.quit()

















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



