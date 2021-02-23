from selenium import webdriver
import time
import unittest
from Conduit.Pages.settingsPage import Settings
from Conduit.Pages.signInPage import SignIn

class LogoutTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_logout(self):
        driver = self.driver

        driver.get("http://react-redux.realworld.io/#/?_k=3ic7hz")

        login = SignIn(driver)
        logout = Settings(driver)

        login.go_to_signin()
        login.enter_username('adammm@wc.pl')
        login.enter_password('12345678')
        login.click_button()

        time.sleep(2)

        logout.go_to_settings()
        time.sleep(5)
        logout.press_logout()

        time.sleep(5)

        # verify if logout
        driver.find_element_by_css_selector("li:nth-of-type(2) > .nav-link").is_displayed()

        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Complete")

if __name__ == '__main__':
    unittest.main()