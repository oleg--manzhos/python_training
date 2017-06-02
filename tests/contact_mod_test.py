from model.contact import Contact


def test_contact_add(app):
    if app.contact.count() == 0:
        app.contact.create(("newly created group"))
    app.contact.modify(Contact("Contact_first_name","Contact_Last_Name", "Contact_Nick_Name"))