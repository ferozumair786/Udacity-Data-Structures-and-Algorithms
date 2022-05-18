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

name_list = ['tim', 'bob', 'azmina', 'jacob', 'sarah', 'luyan', 'admin', 'oracle', 'nero', 'peter parker', 'spiderman', 'jim', 'derek', 'umair', 'amelia', 'miguel', 'astoria']

for name in name_list:
    sub_child.add_user(name)


def is_user_in_group(user=None, group=None):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user and group:

      if type(group) == Group:

        user_list = group.get_users()

        user_list.sort()

        middle = None
        lis = user_list.copy()

        found = False
        while found == False and len(lis) > 1:
          l_mid = round(len(lis)/2)
          middle = lis[l_mid]
          if user == middle:
            found = True
            return found
          elif user > middle:
            lis = lis[l_mid:]
          else:
            lis = lis[0:l_mid]

    else:
        return None

      

    
    

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
#name is at the end of the list
is_user_in_group('umair', sub_child)

# Test Case 2
#user is null
is_user_in_group(sub_child)

# Test Case 3
#group is not a group

is_user_in_group('umair', name_list)