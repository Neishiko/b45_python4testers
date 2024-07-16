# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_modify(app):
    app.session.login(username="admin", password="secret")
    app.contact.first_contact_modify(Contact(firstname="Con", lastname="Tact", mobile="+79998887766", email="con@ta.ct"))
    app.session.logout()
