import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/slider"

class SliderLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_SLIDER = (By.CSS_SELECTOR, ".range-slider__wrap")
    LOCATOR_SLIDER_VALUE_BOX = (By.CSS_SELECTOR, "#sliderValue")
    LOCATOR_SLIDER_VALUE_HOVER = (By.CSS_SELECTOR, ".range-slider__tooltip__label")

class SliderTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_SLIDER_POSITION = "25"