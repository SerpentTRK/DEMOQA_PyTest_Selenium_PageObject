
import time
from selenium.webdriver.common.action_chains import ActionChains

from Data_for_tests.Widgets.slider_testdata import Url, SliderLocators, SliderTestdata
from Methods.methods import Methods

class Slider(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def move_slider(self):
        # Locate the slider element
        slider = self.find_element(SliderLocators.LOCATOR_SLIDER)

        # Получаем длинну слайдера (справочно, чтобы дальше считать положение указателя. По девтулз 258.68
        print(f"Длинна слайдера = {slider.size['width']} pxl")  # Длинна слайдера = 305 pxl

        # Move the slider to 0%
        action = ActionChains(self.browser)
        action.click_and_hold(slider).move_by_offset(-152, 0).release().perform()
        print(f"Положение слайдера установлено на {self.find_element(SliderLocators.LOCATOR_SLIDER_VALUE_HOVER).text}%")

        # Move the slider to 100%
        action.click_and_hold(slider).move_by_offset(152, 0).release().perform()
        print(f"Положение слайдера установлено на {self.find_element(SliderLocators.LOCATOR_SLIDER_VALUE_HOVER).text}%")

        # Move the slider to 50%
        action.click_and_hold(slider).move_by_offset(0, 0).release().perform()
        print(f"Положение слайдера установлено на {self.find_element(SliderLocators.LOCATOR_SLIDER_VALUE_HOVER).text}%")

        # Move the slider to 25%
        action.click_and_hold(slider).move_by_offset(-72, 0).release().perform()
        print(f"Положение слайдера установлено на {self.find_element(SliderLocators.LOCATOR_SLIDER_VALUE_HOVER).text}%")

        # Два варианта получить положение слайдера в %
        # print(self.find_element(SliderLocators.LOCATOR_SLIDER_VALUE_BOX).get_attribute("value"))
        # print(self.find_element(SliderLocators.LOCATOR_SLIDER_VALUE_HOVER).text)

        # последовательность действий с ActionChains, где сначала нажимается и удерживается слайдер, затем перемещается на
        # заданное смещение с помощью move_by_offset, и наконец, он отпускается с помощью release.

    def data_validation(self):
        assert SliderTestdata.DATA_SLIDER_POSITION == self.find_element(SliderLocators.LOCATOR_SLIDER_VALUE_HOVER).text, \
            f"Ошибка: Ожидаемое положение {SliderTestdata.DATA_SLIDER_POSITION} != фактическому {self.find_element(SliderLocators.LOCATOR_SLIDER_VALUE_HOVER).text}"

