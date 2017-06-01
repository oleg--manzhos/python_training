
def test_contact_deletion(app):
    app.session.login("admin", "secret")
    app.contact.delete_first_contact()
    app.session.logout()