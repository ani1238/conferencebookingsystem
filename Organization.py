from User import User


class Organization:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.totalTime = 0

    def get_total_time(self):
        return self.totalTime

    def set_total_time(self, total_time):
        self.totalTime = total_time

    def get_name(self):
        return self.name

    def add_admin_user(self, name, email, role):
        if role == "ADMIN":
            user = User(name, email, role, self)
            self.users.append(user)
            return user
        else:
            print("Organization can only add admins")
            return None

    def add_normal_user(self, admin_user, name, email, role):
        if admin_user.get_role() == "ADMIN":
            user = User(name, email, role, self)
            self.users.append(user)
            return user
        else:
            print("Only admins can add normal users")
            return None

    def get_users(self):
        return self.users
