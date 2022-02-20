from credentials import Credentials


def create_credential(application, username, password, owner):
    """
    Create a credential obj for the user who's trynna add cred.s for an acc.
    :param application:
    :param username:
    :param owner:
    :param password:
    :return:
    """
    new_credentials = Credentials(application, username, password, owner)
    return new_credentials


def get_all_credentials(owner):
    """
    get all the owner's credentials from the array
    :param owner:
    :return:
    """
    return Credentials.owners_credentials(owner)


def add_credentials(credential):
    """
    Save the created user to the list
    :param credential:
    :return:
    """
    return credential.new_credentials()


def get_specific_credentials(name, owner):
    """
    Return a credentials obj with the specified name
    :param name:
    :param owner
    :return:
    """
    return Credentials.find_credentials_by_name(name, owner)
