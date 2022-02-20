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

