

def is_user_in_group(user: str, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == "" or user == None:
        return "Please Provide User"
    return group.has_user(user)
