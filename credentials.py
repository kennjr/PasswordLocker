

class Credentialz:

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
        Credentialz.credentials_list.append(self)

    # The del fun. will delete the contact from all the instances of the class that's why it's a class method
    @classmethod
    def delete_credentials(cls):
        """
        Delete a user (that was passed as a param) from the users list
        :return:
        """
        Credentialz.credentials_list.remove(cls)

    def delete_credential_from_instance(self):
        """
        Delete the credential from the instance
        :return:
        """
        Credentialz.credentials_list.remove(self)

    # CLs indicates that the method is part of the class i.e Contact
    @classmethod
    def do_credentials_exist(cls, app_name, owner):
        """
        Check whether a user exists based on the name param passed
        :param app_name:
        :param owner
        :return: boolean
        """
        for credential in cls.credentials_list:
            if credential.application == app_name and credential.owner == owner:
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
            # The credential.owner is a str
            if credential.owner == owner:
                owners_credentials.append(credential)
        return owners_credentials

    # The fun below will
    @classmethod
    def find_credentials_by_app_name(cls, app_name, owner):
        """
        This fun. will return a credential obj if one is found that matches the name and owner arg
        """
        for credential in cls.credentials_list:
            if credential.application == app_name and credential.owner == owner:
                return credential
