import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/checkbox"

class ChrckBoxLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_EXPAND_ALL = (By.CSS_SELECTOR, "#tree-node > div > button.rct-option.rct-option-expand-all")
    LOCATOR_NOTES = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(1) > ol > li:nth-child(1) > span > label")
    LOCATOR_WORKSPACE = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(1) > span > label")
    LOCATOR_GENEGAL = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) > ol > li:nth-child(4) > span > label")

class CheckBoxTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_NOTES = "notes"
    DATA_WORKSPACE = "workspace"
    DATA_REACT = "react"
    DATA_ANGULAR = "angular"
    DATA_VEU = "veu"
    DATA_GENERAL = "general"