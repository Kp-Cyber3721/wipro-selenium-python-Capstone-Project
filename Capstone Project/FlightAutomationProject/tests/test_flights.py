import pytest
import os
import time
from pages.flightsSearch_page import FlightsSearchPage
from utils.excel_reader import get_test_data
from utils.logger import get_logger

logger = get_logger(__name__)
file_path = os.path.abspath("test_data/flight_test_data.xlsx")
test_data = get_test_data(file_path, "Sheet1")

@pytest.mark.parametrize("data", test_data)
def test_flight_booking(driver, data):
    logger.info("Test started")
    search_page = FlightsSearchPage(driver)
    time.sleep(10)
    logger.info("Searching flight")
    results_page = search_page.search_flight(
        data["from_city"],
        data["to_city"],
        data["departure_date"]
    )
    time.sleep(15)
    logger.info("Selecting first flight")
    checkout_page = results_page.click_first_book_now()
    time.sleep(3)
    logger.info("Filling guest details")
    checkout_page.fill_guest_details(data)
    logger.info("Filling passenger details")
    checkout_page.fill_passenger_details(data)
    time.sleep(2)
    logger.info("Selecting payment and accepting terms")
    checkout_page.select_payment_and_accept_terms()
    logger.info("Completing booking")
    invoice_page = checkout_page.complete_booking()
    time.sleep(5)
    logger.info("Downloading invoice")
    invoice_page.download_invoice()
    time.sleep(5)
    logger.info("Verifying invoice page")
    assert "Invoice" in driver.title
    logger.info("Test completed successfully")
