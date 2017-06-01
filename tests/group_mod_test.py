from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group("modified_group_name"))
    #, "modified_header", "modified_footer"))
