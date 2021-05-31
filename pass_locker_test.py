from unittest.case import TestCase
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


    def test_init(self):
        """
        test for case initialization
        """
        self.assertEqual(self.new_credentials.username, "Brian")
        self.assertEqual(self.new_credentials.password, "pass")



    def test_authentication(self):
        """
        Test for the proper authetication for log in purposes
        """
        self.new_credentials.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)
    






    class TestUserData(unittest,TestCase):
        """
        """

        def setUp(self):
            """
            setting up structure before every test
            """
            self.new_user_data = UserData("facebook", "brian", "pass")

        def tearDown(self):
            """
            clean up after running each test
            """
            UserData.user_data_list = []

        def test_init(self):
            """
            test for the case initialization
            """
            
