class SignIn():

    def __init__(self, driver):
        self.driver = driver

        self.go_to_SignIn_css = "li:nth-of-type(2) > .nav-link"
        self.username_css = "[placeholder='Email']"
        self.password_css = "[placeholder='Password']"
        self.signinButton_css = ".btn.btn-lg.btn-primary.pull-xs-right"

    def go_to_signin(self):
        self.driver.find_element_by_css_selector(self.go_to_SignIn_css).click()

    def enter_username(self, username):
        self.driver.find_element_by_css_selector(self.username_css).clear()
        self.driver.find_element_by_css_selector(self.username_css).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_css_selector(self.password_css).clear()
        self.driver.find_element_by_css_selector(self.password_css).send_keys(password)

    def click_button(self):
        self.driver.find_element_by_css_selector(self.signinButton_css).click()






