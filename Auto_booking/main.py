from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from checkout_page import CheckoutPage, QuotePage, ProductPage, BillingPage, OrderPage
import time


chrome_driver_path = Service("D:\Chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
base_url = "https://ovago-hybrid-stage.travel-dev.com/search/IAD-LON/2023-10-08/2023-10-14"


class AutoBooking:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.get(base_url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)
        self.checkout_page = CheckoutPage(driver)
        self.quote_page = QuotePage(driver)
        self.product_page = ProductPage(driver)
        self.billing_page = BillingPage(driver)
        self.order_page = OrderPage(driver)

    def select_quote(self):
        qs = self.quote_page
        qs.button_quote.click()

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

    def ch_click_continue_button(self):
        cp = self.checkout_page
        cp.button_continue.click()

    def ps_click_continue_button(self):
        ps = self.product_page
        ps.button_continue.click()

    def bi_fill_card_info(self):
        bi = self.billing_page
        bi.input_card_number.send_keys("4242")
        bi.input_card_number.send_keys("4242")
        bi.input_card_number.send_keys("4242")
        bi.input_card_number.send_keys("4242")
        bi.input_card_name.send_keys("Eryn K Abbott")
        bi.input_card_month.send_keys("09")
        bi.input_card_year.send_keys("2025")
        bi.input_cvv.send_keys("222")
        bi.button_buy_now.click()

    def get_order_number(self):
        op = self.order_page
        print(op.label_order_number.text)


if __name__ == "__main__":
    ab = AutoBooking(driver, base_url)

    ab.select_quote()
    ab.fill_contact_form()
    ab.fill_passenger_info()
    ab.ch_click_continue_button()
    time.sleep(5)
    ab.ps_click_continue_button()
    time.sleep(5)
    ab.bi_fill_card_info()
    time.sleep(5)
    ab.get_order_number()
    time.sleep(5)

