import os
import time

from Data_for_tests.Elements.upload_and_download_testdata import Url, UploadAndDownloadLocators, UploadAndDownloadTestdata
from Methods.methods import Methods

class UploadAndDownload(Methods):
    def __init__(self, driver):
        self.browser = driver
        self.url = Url
        super().__init__(driver, self.url)
        # self.browser.get(self.url)  # его надо запускать только в теле уникальных методов, которые не описаны на странице methods.py

    def download_and_upload_file(self):
        # self.find_element(UploadAndDownloadLocators.LOCATOR_DOWNLOAD_BUTTON).click()

        self.find_element(UploadAndDownloadLocators.LOCATOR_PICTURE).send_keys(UploadAndDownloadTestdata.file_path)
        time.sleep(3)

    def download_and_upload_validation(self):
        picture = self.find_element(UploadAndDownloadLocators.LOCATOR_UPLOAD_PICTURE_VALIDATION).text
        assert picture.split("\\")[-1] == UploadAndDownloadTestdata.DATA_PICTURE
