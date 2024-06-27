import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/menu"

class MenuLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_MAIN_ITEM_1 = (By.CSS_SELECTOR, "#nav > li:nth-child(1) > a")
    LOCATOR_MAIN_ITEM_2 = (By.CSS_SELECTOR, "#nav > li:nth-child(2) > a")
    LOCATOR_MAIN_ITEM_2_sub_item_1 = (By.CSS_SELECTOR, "#nav > li:nth-child(2) > ul > li:nth-child(1) > a")
    LOCATOR_MAIN_ITEM_2_sub_item_2 = (By.CSS_SELECTOR, "#nav > li:nth-child(2) > ul > li:nth-child(2) > a")
    LOCATOR_MAIN_ITEM_2_SUB_SUB_LIST = (By.CSS_SELECTOR, "#nav > li:nth-child(2) > ul > li:nth-child(3) > a")
    LOCATOR_MAIN_ITEM_2_SUB_SUB_LIST_Sub_Sub_Item_1 = (By.CSS_SELECTOR, "#nav > li:nth-child(2) > ul > li:nth-child(3) > ul > li:nth-child(1) > a")
    LOCATOR_MAIN_ITEM_2_SUB_SUB_LIST_Sub_Sub_Item_2 = (By.CSS_SELECTOR, "#nav > li:nth-child(2) > ul > li:nth-child(3) > ul > li:nth-child(2) > a")

    LOCATOR_MAIN_ITEM_3 = (By.CSS_SELECTOR, "#nav > li:nth-child(3) > a")

class MenuTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """