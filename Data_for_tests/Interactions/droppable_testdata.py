import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/droppable"

class DroppableLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_TAB_SEMPLE = (By.CSS_SELECTOR, "#droppableExample-tab-simple")
    LOCATOR_DRAG_ME = (By.CSS_SELECTOR, "#draggable")
    LOCATOR_SEMPLE_DROP_HERE = (By.CSS_SELECTOR, "#droppableExample-tabpane-simple #droppable")

    LOCATOR_TAB_ASSEPT = (By.CSS_SELECTOR, "#droppableExample-tab-accept")
    LOCATOR_ASSEPTABLE = (By.CSS_SELECTOR, "#acceptable")
    LOCATOR_NOT_ASSEPTABLE = (By.CSS_SELECTOR, "#notAcceptable")
    LOCATOR_ASSEPT_DROP_HERE = (By.CSS_SELECTOR, "#droppableExample-tabpane-accept #droppable")

    LOCATOR_TAB_PREVENT_PROPOGATION = (By.CSS_SELECTOR, "#droppableExample-tab-preventPropogation")
    LOCATOR_PREVENT_PROPOGATION_DRAG_ME = (By.CSS_SELECTOR, "#dragBox")
    LOCATOR_outer_droppable_box_1 = (By.CSS_SELECTOR, "#notGreedyDropBox")
    LOCATOR_inner_droppable_box_1 = (By.CSS_SELECTOR, "#notGreedyInnerDropBox")
    LOCATOR_outer_droppable_box_2 = (By.CSS_SELECTOR, "#greedyDropBox")
    LOCATOR_inner_droppable_box_2 = (By.CSS_SELECTOR, "#greedyDropBoxInner")

    LOCATOR_REVERT_DRAGGABLE = (By.CSS_SELECTOR, "#droppableExample-tab-revertable")
    LOCATOR_REVERT_DRAGGABLE_will_revert = (By.CSS_SELECTOR, "#revertableDropContainer #revertable")
    LOCATOR_REVERT_DRAGGABLE_not_revert = (By.CSS_SELECTOR, "#revertableDropContainer #notRevertable")
    LOCATOR_REVERT_DRAGGABLE_drop_here = (By.CSS_SELECTOR, "#revertableDropContainer #droppable")

class DroppableTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_DROPPED = "Dropped!"