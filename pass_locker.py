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
                 



