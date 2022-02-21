from user2 import User2
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
    new_user = User2(name, password, time_str)
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
    return User2.find_user_by_name(name)


def check_for_existing_user(name):
    """
    Check if there's a user that goes by the name passed, return a boolean
    :param name:
    :return:
    """
    return User2.does_user_exist(name)


def update_current_user_val(user2):
    """
    Change the value of the current_user property to the one in the brackets
    :param user2:
    :return:
    """
    return User2.update_current_user(user2)


def get_current_user_val():
    """
    Returns the value of the current_user property form the class
    :return:
    """
    return User2.get_current_user()
