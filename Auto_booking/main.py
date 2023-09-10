from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from checkout_page import CheckoutPage
import time


chrome_driver_path = Service("D:\Chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
base_url = "https://ovago-hybrid-stage.travel-dev.com/checkout/OF8C8EA89?xp=20037.1"


class AutoBooking:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(base_url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)
        self.checkout_page = CheckoutPage(driver, base_url)

    def fill_contact_form(self):
        cp = self.checkout_page
        cp.input_email.send_keys("tavi.olla@kiv.dev")
        cp.input_phone.send_keys("9074861280")
        cp.input_street.send_keys("1414 Kshlerin Square")
        cp.input_zipcode.send_keys("71429")
        cp.textbox_country.click()
        cp.button_country.click()
        cp.input_city.send_keys("Albuquerque")

    def fill_passenger_info(self):
        cp = self.checkout_page
        cp.input_firstname.send_keys("Eryn")
        cp.input_middlename.send_keys("K")
        cp.input_lastname.send_keys("Abbott")
        cp.radiobuton_gender.click()
        cp.textbox_nationality.click()
        cp.button_nationality.click()
        cp.textbox_bd_month.click()
        cp.button_bd_month.click()
        cp.input_bd_day.send_keys("14")
        cp.input_bd_year.send_keys("2000")

    def click_continue_button(self):
        cp = self.checkout_page
        cp.button_continue.click()
        time.sleep(5)


if __name__ == "__main__":
    ab = AutoBooking(driver, base_url)
    ab.fill_contact_form()
    ab.fill_passenger_info()
    ab.click_continue_button()
