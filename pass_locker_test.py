from main import display_data
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
        self.new_credentials = Credential('brian', '2827')

    def tearDown(self):
        """
        clean up after running each test
        """
        Credential.credential_list = []


    def test_init(self):
        """
        test for case initialization
        """
        self.assertEqual(self.new_credentials.username, "brian")
        self.assertEqual(self.new_credentials.password, "2827")



    def test_authentication(self):
        """
        Test for the proper authetication for log in purposes
        """
        self.new_credentials.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)









class TestUserData(unittest.TestCase):
    '''
    '''


    def setUp(self):
        '''
        set up structure before every test

        '''
        self.new_user_data = UserData("facebook","brian","pass1")


    def tearDown(self):
        '''
        clean up after runnong each test
        '''
        UserData.user_data_list = []



    def test_init(self):
        '''
        Test for test case initialization"
        '''
        self.assertEqual(self.new_user_data.account_name, "facebook")
        self.assertEqual(self.new_user_data.account_username, "brian")
        self.assertEqual(self.new_user_data.account_password, "pass1")

    def test_add_password(self):
        '''
        Testing if the new website and password can be saved
        '''
        self.new_user_data.create_password()
        self.assertEqual(len(UserData.user_data_list),1)



    def test_show_data(self):
        '''
        Testing if the data can be displayed.
        '''
        self.new_user_data.create_password()
        test_this = UserData("twitter","brian", "pass1")
        test_this.create_password()

        found_user_data = UserData("twitter","brian","pass1")
        self.assertEqual(found_user_data.account_name,test_this.account_name)




if __name__ == "__main__":
    unittest.main()







    
 