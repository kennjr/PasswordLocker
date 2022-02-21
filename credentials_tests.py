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



if __name__ == '__main__':
    unittest.main()
