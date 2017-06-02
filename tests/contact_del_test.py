
def test_contact_deletion(app):
    if app.contact.count() == 0:
        app.contact.create(("newly created group"))
    app.contact.delete_first_contact()