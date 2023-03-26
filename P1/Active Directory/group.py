class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = {}
        self.users = {}

    def add_group(self, group):
        self.groups[group] = (group)

    def add_user(self, user):
        self.users[user] = user

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def has_user(self, user):
        return user in self.users
