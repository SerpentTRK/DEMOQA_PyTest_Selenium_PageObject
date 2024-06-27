import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/select-menu"

class SelectMenuLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_SELECT_VALUE = (By.CSS_SELECTOR, "#withOptGroup > div")
    LOCATOR_SELECT_ONE = (By.CSS_SELECTOR, "#selectOne > div")
    LOCATOR_OLD_STYLE_SELECT_MENU_Voilet = (By.CSS_SELECTOR, "#oldSelectMenu > option:nth-child(8)")
    LOCATOR_MULTISELECT_DROP_DOWN = (By.CSS_SELECTOR, "#selectMenuContainer > div:nth-child(8) > div > div > div")
    LOCATOR_MULTISELECT_DROP_DOWN_Del_Black = (By.CSS_SELECTOR, "#selectMenuContainer > div:nth-child(8) > div > div > div > div.css-1hwfws3 > div:nth-child(3) > div > div.css-xb97g8 > svg")
    LOCATOR_STANDARD_MULTI_SELECT = (By.CSS_SELECTOR, "#cars > option:nth-child(1)")

    # не догадался я, как закрепиться этими реальными локаторами в SELECT_VALUE
    # Group_1_option_1 = "#react-select-2-option-0-0"
    # Group_1_option_2 = "#react-select-2-option-0-1"
    # Group_2_option_1 = "#react-select-2-option-1-0"
    # Group_2_option_2 = "#react-select-2-option-1-1"

class SelectMenuTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_SELECT_VALUE_Group1_option1 = "Group 1, option 2"
    DATA_SELECT_VALUE_A_root_option = "A root option"
    DATA_SELECT_ONE_Mr = "Mr."
    DATA_SELECT_ONE_Prof = "Prof."
    DATA_Old_Style_Select_Menu_Voilet = "Voilet"
    DATA_MULTISELECT_DROP_DOWN = ["Blue", "Green"]
    DATA_STANDARD_MULTI_SELECT = "Volvo"

