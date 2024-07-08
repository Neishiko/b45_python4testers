# -*- coding: utf-8 -*-

def test_first_contact_delete(app):
    app.session.login(username="admin", password="secret")
    app.contact.first_contact_delete()
    app.session.logout()

