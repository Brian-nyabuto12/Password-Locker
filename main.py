from pass_locker import Credential
from pass_locker import UserData
import random
import string
import time

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




def main():
    print("Hello Client,Welcome to Password Locker!,")
    print("What is your name?")
    user_name = input('Name:')
    print(f'Hello {user_name}.What would you like to do?')
    while True:
        print("follow the short codes : cc - create a new account, lg - log in, ext - exit")
        short_code = input().lower()

        if short_code== 'cc':
                          print("-"*10)
                          print("username...")
                          username = input()

                          print("password...")
                          password = input()
                          save_credentials(create_credentials(username, password))
                          print('\n')
                          print(f"Your new account with username : '{username}' and password '{password}' has been created successfully")
                          print('\n')

        elif short_code == 'lg':
                         print("Enter username and password to login:")
                         print("-"*50)
                         username = input("Username: ")
                         password = input("Password: ")
                         log_in = authenticate_credentials(username, password)
                         if log_in==0:
                                print("\n")
                                print("Invalid username and/or password")
                                print("-"*25)
                         elif log_in!=0:
                                print("\n")
                                print(f"Welcome {log_in.uname}! What would you like to do?")


