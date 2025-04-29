class UserNotFound(Exception):
    message = "User not found please give correct id"

    def __str__(self):
        return self.message


class CannotCreateUser(Exception):
    message = "Cannot create user please check again"

    def __str__(self):
        return self.message


class CannotDeleteUser(Exception):
    message = "Cannot delete user please check if user exists"

    def __str__(self):
        return self.message
