import random
import string

class SignUp():

    def __init__(self, driver):
        self.driver = driver

        self.go_to_SignUp_css = "li:nth-of-type(3) > .nav-link"
        self.username_css = "[placeholder='Username']"
        self.email_css = "[placeholder='Email']"
        self.password_css = "[placeholder='Password']"
        self.button_css = ".btn.btn-lg.btn-primary.pull-xs-right"

    def goTosignUp(self):
        self.driver.find_element_by_css_selector(self.go_to_SignUp_css).click()

    def enter_exist_username(self, username):
        self.driver.find_element_by_css_selector(self.username_css).clear()
        self.driver.find_element_by_css_selector(self.username_css).send_keys(username)


    def enter_username(self, username):
        random_letter = string.ascii_letters
        n = random.choice(random_letter)

        self.driver.find_element_by_css_selector(self.username_css).clear()
        self.driver.find_element_by_css_selector(self.username_css).send_keys(username + n + n)

    def enter_email(self, email):
        random_letter = string.ascii_letters
        n = random.choice(random_letter)

        self.driver.find_element_by_css_selector(self.email_css).clear()
        self.driver.find_element_by_css_selector(self.email_css).send_keys(email + n +n)

    def enter_password(self, password):
        self.driver.find_element_by_css_selector(self.password_css).clear()
        self.driver.find_element_by_css_selector(self.password_css).send_keys(password)

    def press_button(self):
        self.driver.find_element_by_css_selector(self.button_css).click()


