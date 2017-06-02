class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.goto_contact_creation()
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nick_name)
        wd.find_element_by_name("submit").click()
        self.app.goto_home_page()

    def modify(self, contact):
        wd = self.app.wd
        self.init_contact_modification()
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nick_name)
        wd.find_element_by_name("update").click()
        self.app.goto_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def goto_contact_creation(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def init_contact_modification(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title='Edit']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))
