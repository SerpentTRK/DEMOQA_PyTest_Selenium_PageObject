
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

    def reading_tool_tip_messages(self):
        # Находим элемент кнопки "Hower me to see"
        button = self.find_element(ToolTipsLocators.LOCATOR_BUTTON_hover_me_to_see)
        # Выполняем ховер на кнопку
        ActionChains(self.browser).move_to_element(button).perform()
        time.sleep(1)
        # Ждем появления всплывающей подсказки
        tooltip_button = self.find_element(ToolTipsLocators.LOCATOR_BUTTON_hover_me_to_see_MESSGE)
        # Получаем текст всплывающей подсказки
        print(tooltip_button.text)


