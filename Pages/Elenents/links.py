import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Data_for_tests.Elements.links_testdata import Url, LinksLocators, LinksTestdata
from Methods.methods import Methods

class Links(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def following_links_will_open_new_tab(self):
        wait = WebDriverWait(self.browser, 10)  #нужно подготовиться к тому, что придется ждать прогруза нового окна
        original_window = self.browser.current_window_handle  #сохранили дискриптор главного окна
        # обычныа ссылка
        self.find_element(LinksLocators.LOCATOR_SIMPLE_LINK).click()  #перешли по ссылке
        wait.until(EC.number_of_windows_to_be(2))  #ждем пока окно гарантированно прогрузится
        self.browser.switch_to.window(self.browser.window_handles[1])  #переключились на новый таб
        self.browser.close()  #закрываем новый таб
        self.browser.switch_to.window(original_window) # переключились на главное по дискриптору
        # #динамическая ссылка (генерируется JS)
        self.find_element(LinksLocators.LOCATOR_DYNAMIC_LINK).click()
        wait.until(EC.number_of_windows_to_be(2))
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.close()  # закрываем новый таб
        self.browser.switch_to.window(original_window)

    def following_links_will_send_an_api_call(self):
        self.find_element(LinksLocators.LOCATOR_CREATED).click()
        print(f"{LinksLocators.LOCATOR_CREATED}: {self.check_response()}")

        self.find_element(LinksLocators.LOCATOR_NO_CONTENT).click()
        print(f"{LinksLocators.LOCATOR_NO_CONTENT}: {self.check_response()}")

        self.find_element(LinksLocators.LOCATOR_MOVED).click()
        print(f"{LinksLocators.LOCATOR_MOVED}: {self.check_response()}")

        self.find_element(LinksLocators.LOCATOR_BAD_REQUEST).click()
        print(f"{LinksLocators.LOCATOR_BAD_REQUEST}: {self.check_response()}")

        self.find_element(LinksLocators.LOCATOR_UNAUTHORIZED).click()
        print(f"{LinksLocators.LOCATOR_UNAUTHORIZED}: {self.check_response()}")

        self.find_element(LinksLocators.LOCATOR_FORBIDDEN).click()
        print(f"{LinksLocators.LOCATOR_FORBIDDEN}: {self.check_response()}")

        self.find_element(LinksLocators.LOCATOR_INVALID_URL).click()
        print(f"{LinksLocators.LOCATOR_INVALID_URL}: {self.check_response()}")

    def check_response(self):
        time.sleep(1)
        response = self.find_element(LinksLocators.LOCATOR_LINK_RESPONSE).text

        for key, value in LinksTestdata.DATA_LINKS_RESPONSE.items():
            if key in response:
                return value


