

class Credentials:

    credentials_list = []

    def __init__(self, application, username, password, owner):
        self.application = application
        self.username = username
        self.password = password
        self.owner = owner

    def new_credentials(self):
        """
        Add a new credential to the credentials_list
        :return:
        """
        Credentials.credentials_list.append(self)

    # The del fun. will delete the contact from all the instances of the class that's why it's a class method
    @classmethod
    def delete_credentials(cls):
        """
        Delete a user (that was passed as a param) from the users list
        :return:
        """
        Credentials.credentials_list.remove(cls)

    # CLs indicates that the method is part of the class i.e Contact
    @classmethod
    def do_credentials_exist(cls, name):
        """
        Check whether a user exists based on the name param passed
        :param name:
        :return: boolean
        """
        for user in cls.credentials_list:
            if user.name == name:
                return True

        return False

    @classmethod
    def owners_credentials(cls, owner):
        """
        Return all the credentials in the list that belong to owner
        :param owner:
        :return:
        """
        owners_credentials = []
        for credential in cls.credentials_list:
            if credential.owner == owner:
                owners_credentials.append(credential)
        return owners_credentials

    # The fun below will
    @classmethod
    def find_credentials_by_name(cls, name, owner):
        """
        This fun. will return a credential obj if one is found that matches the name and owner arg
        """
        for credential in cls.credentials_list:
            if credential.name == name and credential.owner == owner:
                return credential
