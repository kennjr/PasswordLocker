class User:
    users_list = []

    def __init__(self, name, password, datetime):
        self.name = name
        self.password = password
        self.datetime = datetime

    def save_user(self):
        """
        Add a new user to the users_list
        :return:
        """
        User.users_list.append(self)
        print("User saved ", self.name)

    # The del fun. will delete the contact from all the instances of the class that's why it's a class method
    @classmethod
    def delete_user(cls):
        """
        Delete a user (that was passed as a param) from the users list
        :return:
        """
        User.users_list.remove(cls)

    # CLs indicates that the method is part of the class i.e Contact
    @classmethod
    def does_user_exist(cls, name):
        """
        Check whether a user exists based on the name param passed
        :param name:
        :return: boolean
        """
        for user in cls.users_list:
            if user.name == name:
                return True

        return False

    @classmethod
    def display_users(cls):
        """
        method that returns the users list
        """
        return cls.users_list

    # The fun below will
    @classmethod
    def find_user_by_name(cls, name):
        """
        This fun. will return a user obj if one is found that matches the name arg
        """
        for user in cls.users_list:
            if user.name == name:
                return user


