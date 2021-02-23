class AddNewPost():

    def __init__(self, driver):
        self.driver = driver

        self.new_post_button_css = "li:nth-of-type(2) > .nav-link"
        self.title_css = "[placeholder='Article Title']"
        self.what_about_css = "fieldset:nth-of-type(2) > .form-control"
        self.article_css = "textarea"
        self.tags_css = "[placeholder='Enter tags']"
        self.publish_css = ".btn"

    def go_to_new_post(self):
        self.driver.find_element_by_css_selector(self.new_post_button_css).click()

    def enter_title(self, title):
        self.driver.find_element_by_css_selector(self.title_css).clear()
        self.driver.find_element_by_css_selector(self.title_css).send_keys(title)

    def enter_what_about(self, what):
        self.driver.find_element_by_css_selector(self.what_about_css).clear()
        self.driver.find_element_by_css_selector(self.what_about_css).send_keys(what)

    def enter_article(self, article):
        self.driver.find_element_by_css_selector(self.article_css).clear()
        self.driver.find_element_by_css_selector(self.article_css).send_keys(article)

    def enter_tags(self, tags):
        self.driver.find_element_by_css_selector(self.tags_css).clear()
        self.driver.find_element_by_css_selector(self.tags_css).send_keys(tags)

    def enter_publish(self):
        self.driver.find_element_by_css_selector(self.publish_css).click()



