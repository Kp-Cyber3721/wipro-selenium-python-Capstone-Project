from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
import time
from datetime import datetime
class CheckoutPage(BasePage):

    TITLE = (By.XPATH, "//select[@x-model='primary_guest.title']")
    FIRST_NAME = (By.XPATH, "//input[@x-model='primary_guest.first_name']")
    LAST_NAME = (By.XPATH, "//input[@x-model='primary_guest.last_name']")
    EMAIL = (By.XPATH, "//input[@x-model='primary_guest.email']")
    COUNTRY_CODE = (By.XPATH, "//select[@x-model='primary_guest.country_code']")
    PHONE = (By.XPATH, "//input[@x-model='primary_guest.phone']")

    DOB_DAY = (By.XPATH, "//select[contains(@x-model,'dob_day')]")
    DOB_MONTH = (By.XPATH, "//select[contains(@x-model,'dob_month')]")
    DOB_YEAR = (By.XPATH, "//select[contains(@x-model,'dob_year')]")
    PASSPORT = (By.XPATH, "//input[@x-model='formData.passengers.adult_0.passport']")
    NATIONALITY = (By.XPATH, "//select[@x-model='formData.passengers.adult_0.nationality']")

    PAY_LATER_RADIO = (By.XPATH,"//div[contains(@class,'radio-container')]//div[contains(@class,'radio-custom')]")
    TERMS_CHECKBOX = (By.XPATH,"//input[@id='terms_accepted']/following-sibling::div[contains(@class,'checkbox-custom')]")
    CONFIRM_BOOKING = (By.XPATH, "//button[@type='submit']")

    def fill_guest_details(self, data):
        self.select_dropdown(self.TITLE, data["title"])
        time.sleep(1)
        self.send_keys(self.FIRST_NAME, data["fname"])
        time.sleep(1)
        self.send_keys(self.LAST_NAME, data["lname"])
        time.sleep(1)
        self.send_keys(self.EMAIL, data["email"])
        time.sleep(1)
        self.select_dropdown(self.COUNTRY_CODE, data["country_code"])
        time.sleep(1)
        self.send_keys(self.PHONE, data["phone"])
        time.sleep(1)

    def fill_passenger_details(self, data):
        dob_day = str(data["dob_day"]).zfill(2)
        dob_month = str(datetime.strptime(data["dob_month"], "%B").month).zfill(2)
        dob_year = str(data["dob_year"])
        self.select_dropdown(self.DOB_DAY, dob_day)
        time.sleep(1)
        self.select_dropdown(self.DOB_MONTH, dob_month)
        time.sleep(1)
        self.select_dropdown(self.DOB_YEAR, dob_year)
        time.sleep(1)
        self.send_keys(self.PASSPORT, data["passport"])
        time.sleep(1)
        self.select_dropdown(self.NATIONALITY, data["nationality"])
        time.sleep(1)

    def select_payment_and_accept_terms(self):
        payment = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.PAY_LATER_RADIO))
        self.driver.execute_script("arguments[0].click();", payment)
        time.sleep(1)
        checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='terms_accepted']/following-sibling::div[contains(@class,'checkbox-custom')]")))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",checkbox)
        checkbox.click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(By.ID, "terms_accepted").is_selected())

    def complete_booking(self):
        self.click(self.CONFIRM_BOOKING)
        from pages.invoice_page import InvoicePage
        return InvoicePage(self.driver)