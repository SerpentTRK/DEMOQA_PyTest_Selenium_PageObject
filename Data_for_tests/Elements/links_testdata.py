import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/links"

class LinksLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_SIMPLE_LINK = (By.ID, "simpleLink")
    LOCATOR_DYNAMIC_LINK = (By.ID, "dynamicLink")
    LOCATOR_CREATED = (By.ID, "created")
    LOCATOR_NO_CONTENT = (By.ID, "no-content")
    LOCATOR_MOVED = (By.ID, "moved")
    LOCATOR_BAD_REQUEST = (By.ID, "bad-request")
    LOCATOR_UNAUTHORIZED = (By.ID, "unauthorized")
    LOCATOR_FORBIDDEN = (By.ID, "forbidden")
    LOCATOR_INVALID_URL = (By.ID, "invalid-url")

    LOCATOR_LINK_RESPONSE = (By.ID, "linkResponse")


class LinksTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_LINKS_RESPONSE = {"201": "Link has responded with staus 201 and status text Created",
                           "204": "Link has responded with staus 204 and status text No Content",
                           "301": "Link has responded with staus 301 and status text Moved Permanently",
                           "400": "Link has responded with staus 400 and status text Bad Request",
                           "401": "Link has responded with staus 401 and status text Unauthorized",
                           "403": "Link has responded with staus 403 and status text Forbidden",
                           "404": "Link has responded with staus 404 and status text Not Found"}