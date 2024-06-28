import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/selectable"

class SelectableLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_TAB_LIST = (By.CSS_SELECTOR, "#demo-tab-list")
    LOCATOR_cras_justo_odi = (By.CSS_SELECTOR, "#verticalListContainer > li:nth-child(1)")
    LOCATOR_cras_justo_odi_selected_validation = (By.CSS_SELECTOR, "#verticalListContainer > li.mt-2.list-group-item.active.list-group-item-action")

    LOCATOR_TAB_GRID = (By.CSS_SELECTOR, "#demo-tab-grid")
    LOCATOR_BOX_ONE = (By.CSS_SELECTOR, "#row1 > li:nth-child(1)")
    LOCATOR_BOX_ONE_selected_validation = (By.CSS_SELECTOR, "#row1 > li.list-group-item.active.list-group-item-action")

class SelectableTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_cras_justo_odio = "Cras justo odio"
    DATA_box_one = "One"