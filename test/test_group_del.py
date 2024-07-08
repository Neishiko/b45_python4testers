# -*- coding: utf-8 -*-

def test_first_group_delete(app):
    app.session.login(username="admin", password="secret")
    app.group.first_group_delete()
    app.session.logout()
