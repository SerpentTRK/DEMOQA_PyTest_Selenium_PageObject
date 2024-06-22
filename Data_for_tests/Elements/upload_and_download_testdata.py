import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/upload-download"

class UploadAndDownloadLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "#downloadButton")
    LOCATOR_PICTURE = (By.CSS_SELECTOR, "#uploadFile")
    LOCATOR_UPLOAD_PICTURE_VALIDATION = (By.CSS_SELECTOR, "#uploadedFilePath")


class UploadAndDownloadTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    current_dir = os.getcwd()  # Получаем текущий рабочий каталог
    file_path = os.path.join(current_dir, "resources", "1518.jpg")  # Формируем путь к файлу в папке files
    DATA_PICTURE = "1518.jpg"


