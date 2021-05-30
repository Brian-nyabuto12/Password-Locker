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

      