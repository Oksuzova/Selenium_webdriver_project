
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome


class Page(object):
    def __init__(self, driver: Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_element_visible(self, locator: tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

