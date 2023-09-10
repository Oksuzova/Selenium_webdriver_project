from selenium.webdriver.common.by import By


class CheckoutLocators:
    EMAIL_INPUT = (By.NAME, "Checkout[ch_email]")
    VISIBLE_PHONE_INPUT = (By.CSS_SELECTOR, "input[data-at='phone']")
    STREET_INPUT = (By.NAME, "Checkout[ch_address]")
    ZIPCODE_INPUT = (By.NAME, "Checkout[ch_zip]")
    VISIBLE_COUNTRY_TEXTBOX = (By.ID, "select2-checkout-ch_country-container")
    VISIBLE_COUNTRY_BUTTON = (By.CSS_SELECTOR, "#select2-checkout-ch_country-results > li:nth-child(3)")
    CITY_INPUT = (By.NAME, "Checkout[ch_city]")

    FIRST_NAME_INPUT = (By.NAME, "Passenger[0][ps_first_name]")
    MIDDLE_NAME_INPUT = (By.NAME, "Passenger[0][ps_middle_name]")
    LAST_NAME_INPUT = (By.NAME, "Passenger[0][ps_last_name]")
    VISIBLE_GENDER_RADIOBUTTON = (By.CSS_SELECTOR, "#passenger-0-ps_gender > div:nth-child(2) > label.radio__control")
    NATIONALITY_TEXTBOX = (By.ID, "select2-passenger-0-ps_nationality-container")
    VISIBLE_NATIONALITY_BUTTON = (By.CSS_SELECTOR, "#select2-passenger-0-ps_nationality-results > li:nth-child(3)")
    VISIBLE_BIRTHDATE_MONTH_TEXTBOX = (By.ID, "passenger-0-ps_birth_date_month")
    VISIBLE_BIRTHDATE_MONTH_BUTTON = (By.CSS_SELECTOR, "#passenger-0-ps_birth_date_month > option:nth-child(2)")
    BIRTHDATE_DAY_INPUT = (By.NAME, "passenger-0-ps_birth_date_day")
    BIRTHDATE_YEAR_INPUT = (By.NAME, "passenger-0-ps_birth_date_year")

    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#step-itinerary > div.btn-wrapper > button")


class QuoteSelect:
    FIRST_QUOTE_BUTTON = (By.CSS_SELECTOR, "button.sr-price-wrap__book-btn.btn")


class ProductSelect:
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#step-extras > div.btn-wrapper > button")


class BillingInfo:
    CARD_NUMBER_INPUT = (By.NAME, "Checkout[ch_card_number]")
    CARD_NAME_INPUT = (By.NAME, "Checkout[ch_card_name]")
    CARD_EXPIRATION_MONTH_INPUT = (By.NAME, "Checkout[ch_card_expiration_month]")
    CARD_EXPIRATION_YEAR_INPUT = (By.NAME, "Checkout[ch_card_expiration_year]")
    CARD_CVV_INPUT = (By.NAME, "Checkout[ch_card_security_code]")
    BUY_NOW_BUTTON = (By.CSS_SELECTOR, "#step-review > div.checkout-btn-wrapper > button")


class OrderInfo:
    ORDER_NUMDER_TEXT = (By.CSS_SELECTOR, "body > main > div > div.booker-details > div.booker-details__subtitle > span")
