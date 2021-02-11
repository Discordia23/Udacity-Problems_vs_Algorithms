class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)

# additional groups and users
sister = Group('sister')
aunt = Group('aunt')
cousin = Group('cousin')
oncle = Group('oncle')
grandchild = Group('grandchild')
parent.add_group(sister)
sister.add_group(aunt)
sister.add_group(oncle)
aunt.add_group(cousin)
child.add_group(grandchild)
parent.add_user('queen')
sister.add_user('margaret')
sister.add_user('elizabeth')
aunt.add_user('lili')
cousin.add_user('mortimer')
oncle.add_user('bens')
grandchild.add_user('babygirl')

def is_user_in_group(user, group):
    # if user in current group return True
    if user in group.users:
        return True
    # if group has subgroups, recusion call for each subgroup
    if group.get_groups():
        for subgroup in group.get_groups():
            if is_user_in_group(user, subgroup):
                return True
    return False

# Test 1 - given case
print('Test 1:\n', 'Pass' if (is_user_in_group('sub_child_user', parent) == True) else 'Fail')

# Test 2 - added cases
print('Test 2:\n', 'Pass' if (is_user_in_group('margaret', sister) == True) and
      (is_user_in_group('bens', parent) == True) and
      (is_user_in_group('mortimer', child) == False) and
      (is_user_in_group('sub_child_user', aunt) == False) and
      (is_user_in_group('bens', child) == False)
      else 'Fail')

# Test 3 - edge case, User is not existing - returns False
print('Test 3:\n', 'Pass' if (is_user_in_group('test', parent) == False) else 'Fail')
