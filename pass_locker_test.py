from pass_locker import Credential
from pass_locker import UserData
import unittest

class Testcredential(unittest.TestCase):
    """
    class instance that test the credentials
    """
    def setUp(self):
        """
        this is a setup structure before every test
        """
        self.new_credentials = Credential('username', 'password')

    def tearDown(self):
        """
        clean up after running each test
        """
        Credential.credential_list = []
            