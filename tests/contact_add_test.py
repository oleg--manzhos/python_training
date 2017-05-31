# -*- coding: utf-8 -*-


def test_contact_add(app):
    app.session.login("admin", "secret")
    app.contact.create("Contact_first_name","Contact_Last_Name", "Contact_Nick_Name")
    app.session.logout()