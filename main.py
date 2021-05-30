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
    