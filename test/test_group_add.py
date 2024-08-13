# -*- coding: utf-8 -*-
from model.group import Group


def test_group_add(app):
    app.group.create(Group(name="rndm2", header="123", footer="321"))


def test_empty_group_add(app):
    app.group.create(Group(name="", header="", footer=""))
