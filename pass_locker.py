class Credential:
     
     credential_list=[]
     """
     class that generates new instance of credential
     """
     def __init__(self, username,password):
         """
         """
         self.username=username
         self.password=password

     def save_credential(self) :
         """
         """
         Credential.credential_list.append(self)


     @classmethod
     def credential_exist(cls, username, password):
         """
         this method will check if the username exists
         """
         for credential in cls.credential_list:
             if credential.username==username and credential.password==password:
                 return True
             return False       


     @classmethod 
     def authenticate_credential(cls, username, password):
         """
         checks if the usename and password are correct
         """
         for credential in cls.credential_list:
             if credential.username==username and credential.password==password:
                 return credential
             return 0 


class UserData:
    """
    class instance that generate new instance of user data
    """
    user_data_list= []
    user_data_list2= str(user_data_list)

    def __init__(self, account_name, account_username, account_password):
        """
        """
        self.account_name = account_name
        self.account_username = account_username
        self.account_password = account_password

    def create_password(self):
        """
        """
        return UserData.user_data_list.append(self)

    @classmethod
    def display_user_data(cls):
        """
        display all password and account details
        """
        return cls.user_data_list

    @classmethod
    def find_by_account_name(cls, account_name):
        for found in cls.user_data_list2:
            if found == account_name:
                return found
        else:
             print("invalid account name") 

    @classmethod
    def data_exists(cls, account_name):
        """
        this function checks if data exists
        """
        for data in cls.user_data_list:
            if data.account_name ==account_name:
                return data
        else:
            print("data does not exist")
            
                                   

                     




