# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contact_add(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="John", lastname="Ceena", mobile="12356347856", email="john@ceena.ee"))
    app.logout()
