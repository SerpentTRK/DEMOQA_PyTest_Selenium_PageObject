import pytest
from selenium import webdriver


@pytest.fixture(scope="class")  # запускаем один раз за тестовую сессию
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()