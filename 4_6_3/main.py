from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_autoriz_yandex(self):
        driver = self.driver
        driver.get("https://passport.yandex.ru/auth/")

        login = "***@***.**"
        password = "*******"
        element = driver.find_element(By.CLASS_NAME, 'AuthLoginInputToggle-type')
        driver.implicitly_wait(1)
        element.click()
        elem = driver.find_element(By.ID, "passp-field-login")
        driver.implicitly_wait(1)
        elem.send_keys(login)
        elem1 = driver.find_element(By.ID, "passp:sign-in")
        driver.implicitly_wait(1)
        elem1.click()
        driver.implicitly_wait(1)
        elem2 = driver.find_element(By.ID, "passp-field-passwd")
        driver.implicitly_wait(1)
        elem2.send_keys(password)
        driver.implicitly_wait(1)
        elem3 = driver.find_element(By.ID, "passp:sign-in")
        driver.implicitly_wait(1)
        elem3.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


