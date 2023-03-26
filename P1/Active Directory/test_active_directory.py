from group import Group
from active_directory import is_user_in_group
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


print(is_user_in_group(sub_child_user, sub_child))
# TRUE


print(is_user_in_group(sub_child_user, child))
# FALSE


print(is_user_in_group('', child))
# 'Please Provide User'
print(is_user_in_group(None, child))
# 'Please Provide User'
