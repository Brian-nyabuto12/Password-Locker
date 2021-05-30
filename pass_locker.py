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
     def credential_exist(cls,username):
         """
         this method will check if the username exists
         """
         for credential in cls.credential_list:
             if credential.username==username:
                 return True
             return False       


