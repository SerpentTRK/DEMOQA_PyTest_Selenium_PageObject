import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/tool-tips"

class ToolTipsLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_BUTTON_hover_me_to_see = (By.CSS_SELECTOR, "#toolTipButton")
    LOCATOR_BUTTON_hover_me_to_see_MESSGE = (By.CSS_SELECTOR, "#buttonToolTip")


class ToolTipsTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """