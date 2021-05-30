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

def save_credentials(username, password):
    """
    function that saves the credentials
    """
    return Credential.save_credential(username, password)  

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
        print("follow the short input : cc - create a new account, lg - log in, ext - exit")
        short_code = input().lower()

        if short_code== 'cc':
                          print("-"*10)
                          print("username...")
                          username = input()

                          print("password...")
                          password = input()
                          Credential.save_credential( username)
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
                         elif log_in!=username:
                                print("\n")
                                print(f"Welcome {username}! What would you like to do?")



        while True:
                                    print("To change your credentials use the short input : ap - add new password, cp - copy a  password , lp - view you passwords, ex - exit")
                                    short_code= input()  
                                    if short_code== "ap":
                                        print("Enter account name such as facebook, instagram or Gmail:.......")
                                        account_name = input()
                                        print(f"Enter username account for {account_name}.......")
                                        account_username = input()
                                        print("What is you preferred password length?")
                                        pass_length = int(input("Password length:"))
                                        account_password = (pass_length)
                                        create_new_data(user_data(account_name, account_username, account_password))
                                        print("\nHold on tight....")
                                        time.sleep(1.0)
                                        print("\n")
                                        print(f"Generated  password for {account_name} is {account_password}")
                                        print(".."*10)

                                    elif short_code =="cp":
                                        print("Enter the account name of  password you want to copy")
                                        get_name = (input("acc name : "))
                                        if data_exist(get_name):
                                            (account_password)
                                            print("\n")
                                            print(f"Password for  {account_name} successfully copied to clipboard, go ahead and paste it")
                                        else:
                                            print("You do not have any passwords yet")
                                            print("--"*10)



                                    elif short_code == "lp":
                                        if display_data():
                                            print('\n')
                                            for data in  display_data():
                                                print(f"{data.account_name}------> {data.account_password}")
                                                print('\n')

                                    elif short_code == "ext":
                                        print('\n')
                                        print(f"Bye: {username}")







if __name__=='__main__':
    main()