from selenium import webdriver
import time
import unittest
from Conduit.Pages.signInPage import SignIn
from Conduit.Pages.addNewPost import AddNewPost

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_publish_article(self):
        driver = self.driver

        driver.get("http://react-redux.realworld.io/#/?_k=3ic7hz")

        login = SignIn(driver)
        publish = AddNewPost(driver)

        login.go_to_signin()
        login.enter_username('adammm@wc.pl')
        login.enter_password('12345678')
        login.click_button()

        time.sleep(2)

        publish.go_to_new_post()
        publish.enter_title('New test post')
        publish.enter_what_about('test test')
        publish.enter_article\
            ('Lorem Ipsum is simply dummy text of the printing '
             'and typesetting industry. Lorem Ipsum has been the industry')
        publish.enter_tags('#test')
        publish.enter_publish()

        time.sleep(1)
        driver.current_url.__contains__('article')

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")

if __name__ == '__main__':
    unittest.main()