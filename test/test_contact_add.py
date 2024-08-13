# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_add_name_lastname(app):
    app.contact.create(Contact(firstname="John", lastname="Ceena"))


def test_contact_add_name_mobile(app):
    app.contact.create(Contact(firstname="John", mobile="12356347856"))


def test_contact_add_name_email(app):
    app.contact.create(Contact(firstname="John", email="john@ceena.ee"))


def test_contact_add(app):
    app.contact.create(Contact(firstname="John", lastname="Ceena", mobile="12356347856", email="john@ceena.ee"))
