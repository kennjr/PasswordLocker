
from user import User
from user import User
import datetime


def create_user(name, password):
    """
    Create a user obj for the user who's trynna create an acc.
    :param name:
    :param password:
    :return:
    """
    current_time = datetime.datetime.now()
    time_str = str(current_time)
    new_user = User(name, password, time_str)
    return new_user


def save_user(new_user):
    """
    Save the user that's passed as a param
    :param new_user:
    :return:
    """
    new_user.save_user()


def del_user(user):
    """
    Delete the user that's been passed as a param
    :param user:
    :return:
    """
    user.delete_user()


def find_user(name):
    """
    Search for user using the search str passed
    :param name:
    :return:
    """
    return User.does_user_exist(name)
