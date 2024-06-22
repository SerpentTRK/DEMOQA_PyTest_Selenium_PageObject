import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/alerts"

class AlertsLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_ALERT = (By.CSS_SELECTOR, "button#alertButton")
    LOCATOR_ALERT_AFTER_5_SEC_TIMER = (By.CSS_SELECTOR, "button#timerAlertButton")
    LOCATOR_ALERT_CONFIRM = (By.CSS_SELECTOR, "button#confirmButton")
    LOCATOR_ALERT_PROMPT = (By.CSS_SELECTOR, "button#promtButton")



class AlertsTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """