from page import Page
from locators import CheckoutLocators


class CheckoutPage(Page):

    @property
    def input_email(self):
        return self.driver.find_element(*CheckoutLocators.EMAIL_INPUT)

    @property
    def input_phone(self):
        return self.is_element_visible(CheckoutLocators.VISIBLE_PHONE_INPUT)

    @property
    def input_street(self):
        return self.driver.find_element(*CheckoutLocators.STREET_INPUT)

    @property
    def input_zipcode(self):
        return self.driver.find_element(*CheckoutLocators.ZIPCODE_INPUT)

    @property
    def textbox_country(self):
        return self.is_element_visible(CheckoutLocators.VISIBLE_COUNTRY_TEXTBOX)

    @property
    def button_country(self):
        return self.is_element_visible(CheckoutLocators.VISIBLE_COUNTRY_BUTTON)

    @property
    def input_city(self):
        return self.driver.find_element(*CheckoutLocators.CITY_INPUT)

    @property
    def input_firstname(self):
        return self.driver.find_element(*CheckoutLocators.FIRST_NAME_INPUT)

    @property
    def input_middlename(self):
        return self.driver.find_element(*CheckoutLocators.MIDDLE_NAME_INPUT)

    @property
    def input_lastname(self):
        return self.driver.find_element(*CheckoutLocators.LAST_NAME_INPUT)

    @property
    def radiobuton_gender(self):
        return self.is_element_visible(CheckoutLocators.VISIBLE_GENDER_RADIOBUTTON)

    @property
    def textbox_nationality(self):
        return self.driver.find_element(*CheckoutLocators.NATIONALITY_TEXTBOX)

    @property
    def button_nationality(self):
        return self.is_element_visible(CheckoutLocators.VISIBLE_NATIONALITY_BUTTON)

    @property
    def textbox_bd_month(self):
        return self.is_element_visible(CheckoutLocators.VISIBLE_BIRTHDATE_MONTH_TEXTBOX)

    @property
    def button_bd_month(self):
        return self.is_element_visible(CheckoutLocators.VISIBLE_BIRTHDATE_MONTH_BUTTON)

    @property
    def input_bd_day(self):
        return self.driver.find_element(*CheckoutLocators.BIRTHDATE_DAY_INPUT)

    @property
    def input_bd_year(self):
        return self.driver.find_element(*CheckoutLocators.BIRTHDATE_YEAR_INPUT)

    @property
    def button_continue(self):
        return self.driver.find_element(*CheckoutLocators.CONTINUE_BUTTON)
