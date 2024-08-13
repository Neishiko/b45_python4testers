# -*- coding: utf-8 -*-
from model.contact import Contact


def test_first_contact_delete(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Rndm first name"))
    app.contact.first_contact_delete()
