from group import Group
from active_directory import is_user_in_group
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def test_user_in_group():

    assert (is_user_in_group(sub_child_user, sub_child))


def test_user_not_in_group():

    assert (is_user_in_group(sub_child_user, child) == False)


def test_user_not_provided():

    assert (is_user_in_group('', child) == 'Please Provide User')
    assert (is_user_in_group(None, child) == 'Please Provide User')
