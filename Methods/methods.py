import os

import requests
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from twocaptcha import TwoCaptcha


class Methods():
    """
    Класс содержит БАЗОВЫЕ методы
    """
    def __init__(self, driver, url=None):
        self.browser = driver
        self.url = url
        self.browser.get(self.url)

    def captcha_solution(self):
        solver = TwoCaptcha("20459d860ea339a92a31918f1b2f8c42")

    def go_to_site(self):
        """
        Метод для перехода на сайт и больше никаких действий
        """
        return self.browser.get(self.url)

    def scroll_down_page(self, pixels):
        """
        Метод для скроллинга страницы
        """
        self.browser.execute_script(f"window.scrollBy(0,{pixels})")

    def change_window_size(self, x, y):
        """
        Метод для изменения размера экрана. Чтоьбы избежать перекрытия элементов полезно увеличить размер браузера
        """
        self.browser.set_window_size(x, y)

    def script_for_using_closed_element(self, closed_element):
        """
        Если элемент перекрыт другим элементом, то мы можем взаимодействовать с ним используя ява-скрипт
        """
        self.browser.execute_script("arguments[0].click();", closed_element)

    def find_element(self, locator, time=10):
        # return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))
        try:
            return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не был найден на странице {self.url} за {time} секунд")
            return None

    def find_elements(self, locator, time=10):
        try:
            return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не был найден на странице {self.url} за {time} секунд")
            return None

    def check_broken_images(self, image):
        width = self.browser.execute_script("return arguments[0].naturalWidth", image)
        height = self.browser.execute_script("return arguments[0].naturalHeight", image)

        if width == 0 or height == 0:
            return "broken image"
        else:
            return "valid image"

    def check_links_status_code(self, link):
        response = requests.head(link)
        return response.status_code



# class SingleMethods():
#     """
#     Класс содержит оформленные универсальные методы, для обращения к различным элементам интерфейса
#     """
#
#     def __init__(self, driver, url=None):
#         self.browser = driver
#         self.url = url
#         self.browser.get(self.url)
#
#     def text_box(self, locator, test_data):
#         """
#         Метод для заполнения текстового поля
#         """
#         self.browser.implicitly_wait(10)  # настраиваем не явное ожидание элемента на 10 секунд
#         result = self.browser.find_element(*locator)
#         result.send_keys(test_data)
#
#     def radio_button(self, locator):
#         """
#         Метод для выбра radio-button
#         """
#         self.browser.implicitly_wait(10)  # настраиваем не явное ожидание элемента на 10 секунд
#         result = self.browser.find_element(*locator)
#         result.click()
#
#         # if result.is_selected():
#         #     print("Радиобаттон успешно выбран.")
#         # else:
#         #     print("Возникла проблема: радиобаттон не был выбран.")
#
#     def checkbox(self, locator):
#         """
#         Метод для выбора Checkbox
#         """
#         self.browser.implicitly_wait(10)  # настраиваем не явное ожидание элемента на 10 секунд
#         result = self.browser.find_element(*locator)
#         result.click()
#
#     def button(self, locator):
#         """
#         Метод для нажатия кнопок
#         """
#         self.browser.implicitly_wait(10)  # настраиваем не явное ожидание элемента на 10 секунд
#         result = self.browser.find_element(*locator)
#         result.click()
#
#     def data_picker(self, date_locator, year_locator, year_data, month_locator, month_data, day_locator):
#         """
#         Метод для заполнения data-picker
#         """
#         self.browser.implicitly_wait(10)  # настраиваем не явное ожидание элемента на 10 секунд
#         date_of_birth = self.browser.find_element(*date_locator)
#         date_of_birth.click()
#         year_dropdown = Select(self.browser.find_element(*year_locator))
#         year_dropdown.select_by_visible_text(year_data)
#         month_dropdown = Select(self.browser.find_element(*month_locator))
#         month_dropdown.select_by_visible_text(month_data)
#         day_dropdown = self.browser.find_element(*day_locator)
#         day_dropdown.click()
#
#     def upload_and_download(self, locator, file_path):
#         """
#         Метод для загрузки файлов Upload and Download
#         """
#         self.browser.implicitly_wait(10)  # настраиваем не явное ожидание элемента на 10 секунд
#         result = self.browser.find_element(*locator)
#         result.send_keys(file_path)
#
#     def widget_auto_complite(self, locator, file_path):
#         """
#         Метод для заполнения виджета Auto Complete
#         """
#         self.browser.implicitly_wait(10)  # настраиваем не явное ожидание элемента на 10 секунд
#         subjects = self.browser.find_element(*locator)
#         subjects.send_keys(file_path)
#         subjects.send_keys(Keys.RETURN)
#
#     def widget_select_menu_one(self, locator, data_locator):
#         """
#         Метод для выбора одиночного значения из меню типа Select Menu
#         """
#         self.browser.implicitly_wait(10)  # настраиваем не явное ожидание элемента на 10 секунд
#         elem_location = self.browser.find_element(*locator)
#         elem_location.click()
#
#         choice_data = self.browser.find_element(*data_locator)
#         choice_data.click()
