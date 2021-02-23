from selenium import webdriver
import time
import unittest
from Conduit.Pages.signUpPage import SignUp


class RegisterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_register(self):
        driver = self.driver

        driver.get("http://react-redux.realworld.io/#/?_k=3ic7hz")

        register = SignUp(driver)

        register.goTosignUp()
        register.enter_exist_username('758765ieorowruyr')
        register.enter_email('qwadrian@ww.pl')
        register.enter_password('1234')
        register.press_button()

        time.sleep(5)

        # verify if message "password is too short (minimum is 8 characters)" is displayed

        driver.find_element_by_xpath("//div[contains(.,'password is too short (minimum is 8 characters)')]").is_displayed()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")


if __name__ == '__main__':
    unittest.main()