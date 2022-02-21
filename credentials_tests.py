import unittest
from credentials import Credentialz


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def setUp(self) -> None:
        self.new_credentials = Credentialz("myapp", "userone", "password", "user1")

    def tearDown(self) -> None:
        Credentialz.credentials_list = []

    def test_save_credentials(self):
        """
        Check whether the new_credentials is added to the list
        :return:
        """
        length = len(Credentialz.credentials_list)
        self.new_credentials.new_credentials()
        # Compare the old length and new length of the list using the assertEqual
        self.assertEqual(len(Credentialz.credentials_list), length + 1)

    def test_delete_a_user(self):
        """
        Delete a credentials obj form the list and check whether it returns the array-1
        :return:
        """
        self.new_credentials.new_credentials()
        new_user_2 = Credentialz("twitter", "userone", "1234", "user1")
        new_user_2.new_credentials()
        initial_length = len(Credentialz.credentials_list)
        new_user_2.delete_credential_from_instance()
        self.assertEqual(len(Credentialz.credentials_list), initial_length - 1)

    def test_display_users(self):
        """
        Get all the credentials in the list and return them
        :return:
        """
        self.new_credentials.new_credentials()
        self.assertEqual(Credentialz.owners_credentials("user1"), Credentialz.credentials_list)

    def test_find_cred_by_app_name(self):
        """
        Get credentials based on app_name that's been passed
        :return:
        """
        self.new_credentials.new_credentials()
        new_user_2 = Credentialz("twitter", "userone", "1234", "user1")
        new_user_2.new_credentials()
        self.assertEqual(new_user_2, Credentialz.find_credentials_by_app_name("twitter", "user1"))

    def test_do_cred_exist(self):
        """
        Check whether a cred that was added exists
        :return:
        """
        self.new_credentials.new_credentials()
        new_user_2 = Credentialz("twitter", "userone", "1234", "user1")
        new_user_2.new_credentials()
        self.assertTrue(Credentialz.do_credentials_exist("twitter", "user1"))




if __name__ == '__main__':
    unittest.main()
