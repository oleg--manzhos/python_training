from model.contact import Contact


def test_contact_add(app):
    app.contact.modify(Contact("Contact_first_name","Contact_Last_Name", "Contact_Nick_Name"))