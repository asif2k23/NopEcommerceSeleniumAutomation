import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_registration(self):
        self.driver.find_element(By.CSS_SELECTOR, "body > div.master-wrapper-page > div.header > div.header-upper > div.header-links-wrapper > div.header-links > ul > li:nth-child(1) > a").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "gender-male").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "FirstName").send_keys("John")
        time.sleep(1)
        self.driver.find_element(By.ID, "LastName").send_keys("Doe")
        time.sleep(1)
        self.driver.find_element(By.NAME, "DateOfBirthDay").send_keys("20")
        time.sleep(1)
        self.driver.find_element(By.NAME, "DateOfBirthMonth").send_keys(str("May"))
        time.sleep(1)
        self.driver.find_element(By.NAME, "DateOfBirthYear").send_keys("1995")
        time.sleep(1)
        self.driver.find_element(By.ID, "Email").send_keys("john.doe4@example.com")
        time.sleep(1)
        self.driver.find_element(By.ID, "Company").send_keys("Brainstation-23")
        time.sleep(1)
        self.driver.find_element(By.ID, "Newsletter").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "Password").send_keys("pass@1234")
        time.sleep(1)
        self.driver.find_element(By.ID, "ConfirmPassword").send_keys("pass@1234")
        time.sleep(1)
        self.driver.find_element(By.ID, "register-button").click()


        success_message = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "result"))).text
        self.assertEqual(success_message, "Your registration completed")

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
