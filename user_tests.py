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

if __name__ == '__main__':
    unittest.main()
