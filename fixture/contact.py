from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.accept_next_alert = None
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(
                wd.find_elements(By.XPATH, "//input[@value='Send e-Mail']")) > 0):
            wd.find_element(By.LINK_TEXT, "home").click()

    def open_contacts_create_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_create_page()
        # create contact
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element(By.NAME, "submit").click()

    def first_contact_delete(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.accept_next_alert = True
        self.close_alert()
        wd.find_element(By.LINK_TEXT, "home").click()

    def first_contact_modify(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element(By.NAME, "update").click()
        wd.find_element(By.LINK_TEXT, "home page").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def close_alert(self):
        try:
            alert = self.app.wd.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
        finally:
            self.accept_next_alert = True

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements(By.NAME, "selected[]"))
