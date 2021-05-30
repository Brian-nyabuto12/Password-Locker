from pass_locker import Credential
from pass_locker import UserData


def create_credentials(username, password):
    """
    function that create new credentials
    """
    new_credential = Credential(username, password)
    return new_credential

def save_credentials(credential):
    """
    function that saves the credentials
    """
    credential.save_credentials()  

def check_existing_credentials(username, password):
    """
    function to test if the credentias exist
    """
    return Credential.credential_exist(username, password)

def authenticate_credentials(username, password):
    """
    """
    return Credential.authenticate_credential(username, password) 

def  user_data(account_name, account_username, account_password):
    """
    functions to authenticate and log in a user
    """          
    data = UserData(account_name, account_username, account_password)
    return data
def create_new_data(mydata):
    """
    function that create new data to save user password
    """
    mydata.create_password()

def display_data():
    """
    function to display the data
    """
    return UserData.display_user_data()

def data_exist(account_name):
    """
    function that checks that the data exists
    """
    return UserData.data_exists(account_name)

def find_user_data(account_name):
    """
    function that finds the user data by the username
    """
    return UserData.find_by_account_name(account_name)