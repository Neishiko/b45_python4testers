from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def return_to_contacts_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
        # init group greation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def create_contact(self, contact):
        wd = self.wd
        self.open_contacts_create_page()
        # create contact
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        # submit contact creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_contacts_page()

    def open_group_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def open_contacts_create_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
