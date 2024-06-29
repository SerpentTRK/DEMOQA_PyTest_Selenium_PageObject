import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/dragabble"

class DragabbleLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_TAB_SIMPLE = (By.CSS_SELECTOR, "#draggableExample-tab-simple")
    LOCATOR_TAB_SIMPLE_drad_me = (By.CSS_SELECTOR, "#dragBox")

    LOCATOR_TAB_AXIS_RESTRICTED = (By.CSS_SELECTOR, "#draggableExample-tab-axisRestriction")
    LOCATOR_TAB_AXIS_RESTRICTED_Only_X = (By.CSS_SELECTOR, "#restrictedX")
    LOCATOR_TAB_AXIS_RESTRICTED_Only_Y = (By.CSS_SELECTOR, "#restrictedY")

    LOCATOR_TAB_CONTAINER_RESTRICTED = (By.CSS_SELECTOR, "#draggableExample-tab-containerRestriction")
    LOCATOR_TAB_CONTAINER_RESTRICTED_contained_within_the_box = (By.CSS_SELECTOR, "#containmentWrapper > div")
    LOCATOR_TAB_CONTAINER_RESTRICTED_contained_within_my_parent = (By.CSS_SELECTOR, "#draggableExample-tabpane-containerRestriction > div.draggable.ui-widget-content.m-3 > span")

    LOCATOR_TAB_CURSOR_STYLE = (By.CSS_SELECTOR, "#draggableExample-tab-cursorStyle")
    LOCATOR_TAB_CURSOR_STYLE_cursorCenter = (By.CSS_SELECTOR, "#cursorCenter")
    LOCATOR_TAB_CURSOR_STYLE_cursorTopLeft = (By.CSS_SELECTOR, "#cursorTopLeft")
    LOCATOR_TAB_CURSOR_STYLE_cursorBottom = (By.CSS_SELECTOR, "#cursorBottom")

class DragabbleTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_DROPPED = "Dropped!"