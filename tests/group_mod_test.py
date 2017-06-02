from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group("newly created group"))
    app.group.modify_first_group(Group("modified_group_name"))
