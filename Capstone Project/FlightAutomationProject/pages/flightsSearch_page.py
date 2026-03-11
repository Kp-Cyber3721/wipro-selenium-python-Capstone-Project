from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.flightresult_page import FlightResultsPage

class FlightsSearchPage(BasePage):

    FROM_INPUT = (By.XPATH, "//input[@placeholder='Departure City or Airport']")
    TO_INPUT = (By.ID, "arrival_airport_input")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class,'btn')]")
    DEPARTURE_DATE = (By.NAME, "flights_departure_date")

    def search_flight(self, from_city, to_city, departure_date):
        self.send_keys(self.FROM_INPUT, from_city)
        self.driver.find_element(*self.FROM_INPUT).send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        self.send_keys(self.TO_INPUT, to_city)
        self.driver.find_element(*self.TO_INPUT).send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        date_value = f"{departure_date}-03-2026"
        self.driver.execute_script("arguments[0].value = arguments[1];",
            self.driver.find_element(*self.DEPARTURE_DATE),
            date_value)
        self.click(self.SEARCH_BUTTON)
        return FlightResultsPage(self.driver)