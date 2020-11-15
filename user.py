import pyperclip

class User:
    """
    class that generates a new instance of a user
    """
    user_list=[] #empty user list

    def __init__(self,first_name,username,password,email):

        self.first_name=first_name
        self.username=username
        self.password=password
