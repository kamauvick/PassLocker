import unittest
from util.credentials import credentials


class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_creds = credentials('kamauvick', 'vick3445!')


if __name__ == '__main__':
    unittest.main()
