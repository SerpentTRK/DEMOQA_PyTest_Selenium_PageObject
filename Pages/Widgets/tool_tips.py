
import time
from selenium.webdriver.common.action_chains import ActionChains

from Data_for_tests.Widgets.tool_tips_testdata import Url, ToolTipsLocators, ToolTipsTestdata
from Methods.methods import Methods

class ToolTips(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def reading_and_validation_tool_tip_messages(self):
        # Находим элемент кнопки "Hower me to see"
        button = self.find_element(ToolTipsLocators.LOCATOR_BUTTON_hover_me_to_see)
        # Выполняем ховер на кнопку
        ActionChains(self.browser).move_to_element(button).perform()
        time.sleep(1)
        # Ждем появления всплывающей подсказки
        tooltip_button = self.find_element(ToolTipsLocators.LOCATOR_BUTTON_hover_me_to_see_MESSGE)
        # Получаем текст всплывающей подсказки
        assert tooltip_button.text == ToolTipsTestdata.DATA_BUTTON_hover_me_to_see, \
            f"Ошибка. Должно быть {ToolTipsTestdata.DATA_BUTTON_hover_me_to_see}, а не {tooltip_button.text}"

        #Text box "Hower me to see"
        textbox = self.find_element(ToolTipsLocators.LOCATOR_TEXTBOX_hover_me_to_see)
        # Выполняем ховер на кнопку
        ActionChains(self.browser).move_to_element(textbox).perform()
        time.sleep(1)
        # Ждем появления всплывающей подсказки
        tooltip_textbox = self.find_element(ToolTipsLocators.LOCATOR_TEXTBOX_hover_me_to_see_MESSGE)
        # Получаем текст всплывающей подсказки
        assert tooltip_textbox.text == ToolTipsTestdata.DATA_TEXTBOX_hover_me_to_see, \
            f"Ошибка. Должно быть {ToolTipsTestdata.DATA_TEXTBOX_hover_me_to_see}, а не {tooltip_textbox.text}"

        # Text from textbox "Contrary"
        contrary = self.find_element(ToolTipsLocators.LOCATOR_CONTAINER_Contrary)
        # Выполняем ховер на кнопку
        ActionChains(self.browser).move_to_element(contrary).perform()
        time.sleep(1)
        # Ждем появления всплывающей подсказки
        tooltip_contrary = self.find_element(ToolTipsLocators.LOCATOR_CONTAINER_Contrary_MESSAGE)
        # Получаем текст всплывающей подсказки
        assert tooltip_contrary.text == ToolTipsTestdata.DATA_CONTAINER_Contrary, \
            f"Ошибка. Должно быть {ToolTipsTestdata.DATA_CONTAINER_Contrary}, а не {tooltip_contrary.text}"

        # Text from textbox "1.10.32"
        numbers = self.find_element(ToolTipsLocators.LOCATOR_CONTAINER_numbers)
        # Выполняем ховер на кнопку
        ActionChains(self.browser).move_to_element(numbers).perform()
        time.sleep(1)
        # Ждем появления всплывающей подсказки
        tooltip_numbers = self.find_element(ToolTipsLocators.LOCATOR_CONTAINER_numbers_MESSAGE)
        # Получаем текст всплывающей подсказки
        assert tooltip_numbers.text == ToolTipsTestdata.DATA_CONTAINER_numbers, \
            f"Ошибка. Должно быть {ToolTipsTestdata.DATA_CONTAINER_numbers}, а не {tooltip_numbers.text}"



