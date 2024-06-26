import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/tool-tips"

class ToolTipsLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_BUTTON_hover_me_to_see = (By.CSS_SELECTOR, "#toolTipButton")
    LOCATOR_BUTTON_hover_me_to_see_MESSGE = (By.CSS_SELECTOR, "#buttonToolTip")
    LOCATOR_TEXTBOX_hover_me_to_see = (By.CSS_SELECTOR, "#toolTipTextField")
    LOCATOR_TEXTBOX_hover_me_to_see_MESSGE = (By.CSS_SELECTOR, "#textFieldToolTip")

    LOCATOR_CONTAINER_Contrary = (By.CSS_SELECTOR, "#texToolTopContainer > a:nth-child(1)")
    LOCATOR_CONTAINER_Contrary_MESSAGE = (By.CSS_SELECTOR, "#contraryTexToolTip")
    LOCATOR_CONTAINER_numbers = (By.CSS_SELECTOR, "#texToolTopContainer > a:nth-child(2)")
    LOCATOR_CONTAINER_numbers_MESSAGE = (By.CSS_SELECTOR, "#sectionToolTip")

class ToolTipsTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_BUTTON_hover_me_to_see = "You hovered over the Button"
    DATA_TEXTBOX_hover_me_to_see = "You hovered over the text field"
    DATA_CONTAINER_Contrary = "You hovered over the Contrary"
    DATA_CONTAINER_numbers = "You hovered over the 1.10.32"