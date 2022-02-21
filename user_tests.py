import unittest
from user2 import User2
import datetime


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def setUp(self) -> None:
        """
        Create a new user every time the user wants to run test(s)
        :return:
        """
        current_time = datetime.datetime.now()
        time_str = str(current_time)
        self.new_user = User2("userone", "password", time_str)

    def tearDown(self) -> None:
        """
        Clear everything once an instance of the tests are done
        :return:
        """
        User2.users_list = []

    def test_save_new_user(self):
        """
        Try saving a new user to the list
        :return:
        """
        # Get the initial length of the user_list
        length = len(User2.users_list)
        self.new_user.save_user()
        # Compare the old length and new length of the list using the assertEqual
        self.assertEqual(len(User2.users_list), length + 1)

    def test_delete_a_user(self):
        """
        Delete a user form the list and check whether it returns the array-1
        :return:
        """
        current_time = datetime.datetime.now()
        time_str = str(current_time)
        self.new_user.save_user()
        new_user_2 = User2("usertwo", "1234", time_str)
        new_user_2.save_user()
        initial_length = len(User2.users_list)
        new_user_2.delete_user_from_instance()
        self.assertEqual(len(User2.users_list), initial_length - 1)

    def test_check_user_existence(self):
        """
        Check whether a user exists in the list if he was added
        :return:
        """
        self.new_user.save_user()
        # We're creating another instance of the contact class below
        test_contact = User2("Testuser", "123", "7123456")  # new contact
        test_contact.save_user()
        user_exists = User2.does_user_exist("userone")
        self.assertTrue(user_exists)

    def test_display_users(self):
        """
        Get all the users in the list and return them
        :return:
        """
        self.new_user.save_user()
        self.assertEqual(User2.display_users(), User2.users_list)

    def test_find_user_by_name(self):
        """
        Search for a user in the user_list then check if the user exists
        :return:
        """
        self.new_user.save_user()
        returned_obj = User2.find_user_by_name("useron")
        user_obj = False
        if returned_obj is not None:
            user_obj = True
        self.assertTrue(user_obj)




if __name__ == '__main__':
    unittest.main()
