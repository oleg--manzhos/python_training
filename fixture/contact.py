class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, first_name, last_name, nick_name):
        wd = self.app.wd
        self.goto_contact_creation()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nick_name)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def goto_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()