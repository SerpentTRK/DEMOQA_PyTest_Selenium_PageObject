
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

    def start_and_stop_slider(self):
        # Locate the slider element
        slider = self.find_element(SliderLocators.LOCATOR_SLIDER)

        # ширина слайдера в пикселях
        slider_width = slider.size['width']
        print(slider_width)

        # Вычисляем количество пикселей, для смещения слайдера на 1%.
        pixels_for_1_percent = slider_width / 100
        print(pixels_for_1_percent)
        # Calculate the number of pixels to move for 25%
        # Чтобы сместиться, например, на 25% мы: pixels_for_1_percent * 25

        # # Move the slider to 0%
        action = ActionChains(self.browser)
        action.click_and_hold(slider).move_by_offset(-142, 0).release().perform()
        print(f"Положение слайдера установлено на {self.find_element(SliderLocators.LOCATOR_SLIDER_VALUE_HOVER).text}%")
        time.sleep(3)

        action.click_and_hold(slider).move_by_offset(142, 0).release().perform()
        print(f"Положение слайдера установлено на {self.find_element(SliderLocators.LOCATOR_SLIDER_VALUE_HOVER).text}%")
        time.sleep(3)

        action.click_and_hold(slider).move_by_offset(-152, 0).release().perform()
        print(f"Положение слайдера установлено на {self.find_element(SliderLocators.LOCATOR_SLIDER_VALUE_HOVER).text}%")
        time.sleep(3)
        # Два варианта получить положение слайдера в %
        # print(self.find_element(SliderLocators.LOCATOR_SLIDER_VALUE_BOX).get_attribute("value"))
        # print(self.find_element(SliderLocators.LOCATOR_SLIDER_VALUE_HOVER).text)

        time.sleep(3)
        # последовательность действий с ActionChains, где сначала нажимается и удерживается слайдер, затем перемещается на
        # заданное смещение с помощью move_by_offset, и наконец, он отпускается с помощью release.



