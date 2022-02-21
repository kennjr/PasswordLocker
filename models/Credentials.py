

class Credential:

    # credentials_list = []

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
        # Credential.credentials_list.append(self)

