import unittest


class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Method to run before each test case
        """
        # Create user object
        pass

    def tearDown(self):
        """
        Clear contact_list
        """
        pass  # Clear user_list

    def test__init__(self):
        """
        Check is class was init
        """
        pass

    def test_login(self):
        pass

    def test_add_user(self):
        """
        Check is the user list is incremented
        """
        pass

    def test_random_pass(self):
        pass

    def test_search_account(self):
        """
        Find if a user exists
        """
        pass

    def test_del_user(self):
        """
        Test deleting a user
        """
        pass


if __name__ == '__main__':
    unittest.main()
