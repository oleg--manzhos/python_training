# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contact_add(app):
    app.login("admin", "secret")
    app.contact_creation("Contact_first_name","Contact_Last_Name", "Contact_Nick_Name")
    app.logout()