# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contact_add(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="John", lastname="Ceena", mobile="12356347856", email="john@ceena.ee"))
    app.session.logout()
