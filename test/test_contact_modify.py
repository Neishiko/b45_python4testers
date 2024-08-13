# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_modify_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Rndm first name"))
    app.contact.first_contact_modify(Contact(firstname="Con"))


def test_contact_modify_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Rndm first name"))
    app.contact.first_contact_modify(Contact(lastname="Tact"))


def test_contact_modify_mobile(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Rndm first name"))
    app.contact.first_contact_modify(Contact(mobile="+79998887766"))


def test_contact_modify_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Rndm first name"))
    app.contact.first_contact_modify(Contact(email="con@ta.ct"))


def test_contact_modify(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Rndm first name"))
    app.contact.first_contact_modify(Contact(firstname="Con", lastname="Tact", mobile="+79998887766", email="con@ta.ct"))
