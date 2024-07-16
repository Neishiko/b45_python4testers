# -*- coding: utf-8 -*-
from model.group import Group


def test_group_add(app):
    app.session.login(username="admin", password="secret")
    app.group.first_group_modify(Group(name="Updating", header="This", footer="Group"))
    app.session.logout()
