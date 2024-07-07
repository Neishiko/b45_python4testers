# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from contact import Contact


class TestContactAdd(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_contact_add(self):
        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstname="John", lastname="Ceena", mobile="12356347856", email="john@ceena.ee"))
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_contacts_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "home").click()

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

    def open_contacts_create_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def login(self, username, password):
        wd = self.wd
        self.open_homepage()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
