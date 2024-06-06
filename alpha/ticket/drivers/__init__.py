from selenium import webdriver
from config.settings import Config


class BrowserManager:
    def __init__(self, browser_type="chrome"):
        if browser_type.lower() == "chrome":
            self.driver = self.setup_chrome()

    def _chrome_options(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = Config.chrome_path
        return chrome_options

    def setup_chrome(self):
        driver = webdriver.Chrome(options=self._chrome_options())
        return driver

    def teardown(self):
        self.driver.quit()
