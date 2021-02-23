from selenium import webdriver
import time
import unittest
from Conduit.Pages.signInPage import SignIn

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver

        driver.get("http://react-redux.realworld.io/#/?_k=3ic7hz")

        login = SignIn(driver)

        login.go_to_signin()
        login.enter_username('samplex@wc.pl')
        login.enter_password('12345678')
        login.click_button()

        time.sleep(2)

        # verify if message "email or password is invalid" is displayed
        driver.find_element_by_xpath("//div[contains(., 'email or password is invalid')]").is_displayed()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")


if __name__ == '__main__':
    unittest.main()