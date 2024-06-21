import time

from Data_for_tests.Elements.broken_links_and_images_testdata import Url, BrokenLinksImagesLocators, BrokenLinksImagesTestdata
from Methods.methods import Methods

class BrokenLinksImages(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def image_validation(self):
        images = self.find_elements(BrokenLinksImagesLocators.LOCATOR_VALID_IMAGE)

        for img in images:
            src = img.get_attribute('src')
            if self.check_broken_images(img) == "broken image":
                print(f"Изображение {src} является битым.")

    def links_validation(self):
        links = self.find_elements(BrokenLinksImagesLocators.LOCATOR_VALID_LINKS)

        for link in links:
            href = link.get_attribute("href")
            if self.check_links_status_code(href) != range(200, 299):
                print(f"Ссылка {href} на странице {self.url} являетя битой. Ожидаемый статус код 201, а полученный {self.check_links_status_code(href)}")
                # тут можно что угодно првоерить... зная какой именно код ответа должен быть...

