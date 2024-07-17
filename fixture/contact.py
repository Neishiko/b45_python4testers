from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.accept_next_alert = None
        self.app = app

    def open_contacts_create_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_create_page()
        # create contact
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        # submit contact creation
        wd.find_element(By.NAME, "submit").click()

    def first_contact_delete(self):
        wd = self.app.wd
        self.accept_next_alert = True
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.close_alert()

    def first_contact_modify(self, contact):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "update").click()

    def close_alert(self):
        try:
            alert = self.app.wd.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
        finally:
            self.accept_next_alert = True
