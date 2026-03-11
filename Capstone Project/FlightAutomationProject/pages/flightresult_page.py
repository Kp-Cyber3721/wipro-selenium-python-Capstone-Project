from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage

class FlightResultsPage(BasePage):
    BOOK_NOW_BUTTON = (By.XPATH,"//button[contains(@class,'btn') and .//span[contains(text(),'Book Now')]]")
    def click_first_book_now(self):
        button = self.wait.until(EC.element_to_be_clickable(self.BOOK_NOW_BUTTON))
        button.click()
        return CheckoutPage(self.driver)