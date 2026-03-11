from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import os
import time
class InvoicePage(BasePage):
    DOWNLOAD = (By.XPATH, "//div[@class='btn light w-full flex items-center justify-start gap-2 cursor-pointer']")
    DOWNLOAD_PATH = "tests/downloads"
    def download_invoice(self, timeout=30):
        try:
            download_btn = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.DOWNLOAD))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", download_btn)
            self.driver.execute_script("arguments[0].click();", download_btn)
            print("Clicked Download Invoice button")
            end_time = time.time() + timeout
            while time.time() < end_time:
                files = os.listdir(self.DOWNLOAD_PATH)
                if files:
                    print(f"Invoice downloaded: {files[0]}")
                    return files[0]
                time.sleep(1)
            raise Exception("Invoice not downloaded within timeout")
        except Exception as e:
            print("Failed to download invoice:", e)
            raise