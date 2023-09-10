
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome


class Page(object):
    def __init__(self, driver: Chrome, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def is_element_visible(self, locator: tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

