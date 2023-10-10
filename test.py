import unittest
from main import gitApi


class TestGetApi(unittest.TestCase):

    def testApi(self):
        self.assertEqual(gitApi("coreyheckel3"), True, 'user id exists')

    def testApi1(self):
        self.assertEqual(gitApi(";'d"), False, 'user does not exist')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

