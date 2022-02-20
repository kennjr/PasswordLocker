from credentials import Credentialz


def create_credential(application, username, password, owner):
    """
    Create a credential obj for the user who's trynna add cred.s for an acc.
    :param application:
    :param username:
    :param owner:
    :param password:
    :return:
    """
    new_credentials = Credentialz(application, username, password, owner)
    return new_credentials


def get_all_credentials(owner):
    """
    get all the owner's credentials from the array
    :param owner:
    :return:
    """
    return Credentialz.owners_credentials(owner)


def add_credentials(credential):
    """
    Save the created user to the list
    :param credential:
    :return:
    """
    return credential.new_credentials()


def get_specific_credentials(app_name, owner):
    """
    Return a credentials obj with the specified name
    :param app_name:
    :param owner
    :return:
    """
    return Credentialz.find_credentials_by_app_name(app_name, owner)


def delete_credential(credential: Credentialz):
    """
    Deletes the credential that's been passed from the array
    :param credential:
    :return:
    """
    return credential.delete_credential_from_instance()
    # Credentialz.delete_credentials()
    # return credential.delete_credentials()
