import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PlaceOrderTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_place_order_as_guest(self):

        self.driver.find_element(By.LINK_TEXT, "Electronics").click()
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Cell phones"))).click()

        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Nokia Lumia 1020"))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "add-to-cart-button-20"))).send_keys("2")
        self.driver.find_element(By.ID, "add-to-cart-button-20").click()

        self.driver.find_element(By.XPATH, "//*[@id='topcartlink']/a/span[1]").click()
        self.driver.find_element(By.ID, "termsofservice").click()
        self.driver.find_element(By.ID, "checkout").click()

        self.driver.find_element(By.XPATH, "//*[@id='main']/div/div/div/div[2]/div[1]/div[1]/div[3]/button[1]").click()

        self.wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("John")
        time.sleep(1)
        self.driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("Doe")
        time.sleep(1)
        self.driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("john.doe@example.com")
        time.sleep(1)
        self.driver.find_element(By.ID, "BillingNewAddress_CountryId").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,"#BillingNewAddress_CountryId option:nth-child(2)").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "BillingNewAddress_StateProvinceId").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#BillingNewAddress_StateProvinceId > option:nth-child(2)").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "BillingNewAddress_City").send_keys("City")
        time.sleep(1)
        self.driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Address 1")
        time.sleep(1)
        self.driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("12345")
        time.sleep(1)
        self.driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("1234567890")
        time.sleep(1)
        self.driver.find_element(By.ID, "billing-buttons-container").click()
        time.sleep(1)

        self.wait.until(EC.visibility_of_element_located((By.ID, "shippingoption_1"))).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='shipping-method-buttons-container']/button").click()
        time.sleep(2)

        self.wait.until(EC.visibility_of_element_located((By.ID, "paymentmethod_1"))).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='payment-method-buttons-container']/button").click()
        time.sleep(2)

        self.wait.until(EC.visibility_of_element_located((By.ID, "CreditCardType"))).send_keys("Visa")
        time.sleep(1)
        self.driver.find_element(By.ID,"CardholderName").send_keys("John Doe")
        time.sleep(1)
        self.driver.find_element(By.ID, "CardNumber").send_keys("4263982640269299")
        time.sleep(1)
        self.driver.find_element(By.ID, "ExpireMonth").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#ExpireMonth > option:nth-child(12)").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "ExpireYear").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#ExpireYear > option:nth-child(5)").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "CardCode").send_keys("837")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='payment-info-buttons-container']/button").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//*[@id='confirm-order-buttons-container']/button").click()
        time.sleep(2)

        success_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".section.order-completed"))).text
        self.assertIn("Your order has been successfully processed!", success_message)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
