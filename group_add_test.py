# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_group_add_test(app):
    app.login("admin", "secret")
    app.create_group(Group("new group name", "new group header", "new group footer"))
    app.logout()