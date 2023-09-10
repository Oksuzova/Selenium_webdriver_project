from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome


class Page(object):
    driver = None
    base_url = None
    wait = None

    def __init__(self, driver: Chrome, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def __new__(cls, *args, **kwargs):
        return cls.__init__(driver=kwargs.get("driver"), base_url=kwargs.get("base_url"))

    def is_element_visible(self, locator: tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

    # @classmethod
    # def _get_obj_by_attr(cls, attrname):
    #     if hasattr(cls, attrname):
    #         return getattr(cls, attrname)

    def __getattr__(self, key: str):
        if hasattr(self, key):
            if key.lower().startswith("visible_"):
                return self.is_element_visible(getattr(self, key))
            else:
                self.driver.find_element(*getattr(self, key))

    def __setattr__(self, key, value):
        setattr(self, key, value)


