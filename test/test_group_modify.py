# -*- coding: utf-8 -*-
from model.group import Group


def test_group_modify_name(app):
    app.group.first_group_modify(Group(name="Updating"))


def test_group_modify_header(app):
    app.group.first_group_modify(Group(header="This"))

def test_group_modify_footer(app):
    app.group.first_group_modify(Group(footer="Group"))


def test_group_modify(app):
    app.group.first_group_modify(Group(name="Updating", header="This", footer="Group"))
