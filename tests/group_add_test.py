# -*- coding: utf-8 -*-
from model.group import Group

def test_group_add_test(app):
    app.session.login("admin", "secret")
    app.group.create(Group("new group name", "new group header", "new group footer"))
    app.session.logout()