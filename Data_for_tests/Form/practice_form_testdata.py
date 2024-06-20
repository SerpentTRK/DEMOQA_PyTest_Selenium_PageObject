import os

from selenium.webdriver.common.by import By

Url = "https://demoqa.com/automation-practice-form"

class PracticeFormLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_FIRST_NAME = (By.ID, "firstName")
    LOCATOR_LAST_NAME = (By.ID, "lastName")
    LOCATOR_EMAIL_FIELD = (By.CSS_SELECTOR, ".col-md-9.col-sm-12 #userEmail")
    LOCATOR_GENDER = (By.CSS_SELECTOR, "[for='gender-radio-1']")
    LOCATOR_MOBILE_NUMBER = (By.CSS_SELECTOR, ".col-md-9.col-sm-12 #userNumber")
    LOCATOR_DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
    LOCATOR_DATE_OF_BIRTH_YEAR = (By.CLASS_NAME, "react-datepicker__year-select")
    LOCATOR_DATE_OF_BIRTH_MONTH = (By.CLASS_NAME, "react-datepicker__month-select")
    LOCATOR_DATE_OF_BIRTH_DAY = (By.XPATH, "//div[@aria-label='Choose Wednesday, January 15th, 2003']")
    LOCATOR_SUBJECTS = (By.ID, "subjectsInput")
    LOCATOR_HOBBIES = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
    LOCATOR_PICTURE = (By.ID, "uploadPicture")
    LOCATOR_CURRENT_ADDRESS = (By.ID, "currentAddress")
    LOCATOR_STATE = (By.ID, "state")
    LOCATOR_STATE_NAME = (By.XPATH, "//div[text()='Rajasthan']")
    LOCATOR_CITY = (By.ID, "city")
    LOCATOR_CITY_NAME = (By.XPATH, "//div[@id='city']//div[contains(text(), 'Jaipur')]")
    LOCATOR_BUTTON_SUBMIT = (By.ID, "submit")

    LOCATOR_DATA_FULL_NAME_VALIDATION = (By.CSS_SELECTOR, "table tbody tr:nth-child(1) td:nth-child(2)")
    LOCATOR_DATA_EMAIL_FIELD_VALIDATOIN = (By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(2) td:nth-child(2)")
    LOCATOR_DATA_GENDER_VALIDATION = (By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(3) td:nth-child(2)")
    LOCATOR_DATA_MOBILE_NUMBER_VALIDATION = (By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(4) td:nth-child(2)")
    LOCATOR_DATA_DATE_OF_BIRTH_VALIDATION = (By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(5) td:nth-child(2)")
    LOCATOR_DATA_SUBJECTS_VALIDATION = (By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(6) td:nth-child(2)")
    LOCATOR_DATA_HOBBIES_VALIDATION = (By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(7) td:nth-child(2)")
    LOCATOR_DATA_PICTURE_FILENAME_VALIDATION = (By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(8) td:nth-child(2)")
    LOCATOR_DATA_CURRENT_ADDRESS_VALIDATION = (By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(9) td:nth-child(2)")
    LOCATOR_DATA_STATE_CITY_VALIDATION = (By.CSS_SELECTOR, ".modal-body table tbody tr:nth-child(10) td:nth-child(2)")

class PracticeFormTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    DATA_FULL_NAME = "Василий Алибабаевич"
    DATA_FIRST_NAME = "Василий"
    DATA_LAST_NAME = "Алибабаевич"
    DATA_EMAIL_FIELD = "vasya@test.ru"
    DATA_GENDER = "Male"
    DATA_MOBILE_NUMBER = "4951112233"
    DATA_DATE_OF_BIRTH = "15 January,2003"
    DATA_DATE_OF_BIRTH_YEAR = "2003"
    DATA_DATE_OF_BIRTH_MONTH = "January"
    DATA_DATE_OF_BIRTH_DAY = "15"
    DATA_SUBJECTS = "Maths"
    DATA_HOBBIES = "Sports"

    current_dir = os.getcwd()  # Получаем текущий рабочий каталог
    file_path = os.path.join(current_dir, "resources", "1518.jpg")  # Формируем путь к файлу в папке files
    DATA_PICTURE = file_path

    DATA_PICTURE_FILENAME = "1518.jpg"
    DATA_CURRENT_ADDRESS = "А/Я 000001, на деревню Дедушке"
    DATA_STATE_CITY = "Rajasthan Jaipur"
