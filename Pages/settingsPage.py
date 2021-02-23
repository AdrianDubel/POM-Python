class Settings():

    def __init__(self, driver):
        self.driver = driver

        self.settings_button_css = "a[href='#settings']"
        self.url_css = "[placeholder='URL of profile picture']"
        self.bio_css = "[rows]"
        self.username_css = "[placeholder='Username']"
        self.email_css = "fieldset:nth-of-type(4) > .form-control.form-control-lg"
        self.new_password_css = "fieldset:nth-of-type(5) > .form-control.form-control-lg"
        self.update_button_css = ".btn.btn-lg.btn-primary.pull-xs-right"
        self.logout_button_css = ".btn.btn-outline-danger"

    def go_to_settings(self):
        self.driver.find_element_by_css_selector(self.settings_button_css).click()

    def enter_url(self, url):
        self.driver.find_element_by_css_selector(self.url_css).clean()
        self.driver.find_element_by_css_selector(self.url_css).send_keys(url)

    def enter_bio(self, text):
        self.driver.find_element_by_css_selector(self.bio_css).clean()
        self.driver.find_element_by_css_selector(self.bio_css).send_keys(text)

    def enter_username(self, username):
        self.driver.find_element_by_css_selector(self.username_css).clean()
        self.driver.find_element_by_css_selector(self.username_css).send_keys(username)

    def enter_email(self, email):
        self.driver.find_element_by_css_selector(self.email_css).clean()
        self.driver.find_element_by_css_selector(self.email_css).send_keys(email)

    def enter_new_password(self, password):
        self.driver.find_element_by_css_selector(self.new_password_css).clean()
        self.driver.find_element_by_css_selector(self.new_password_css).send_keys(password)

    def press_update(self):
        self.driver.find_element_by_css_selector(self.update_button_css).click()

    def press_logout(self):
        self.driver.find_element_by_css_selector(self.logout_button_css).click()


