# -*- coding: utf-8 -*-
import time
from model.contact import Contact


def test_contact_add(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="John", lastname="Ceena", mobile="12356347856", email="john@ceena.ee"))
    app.session.logout()

