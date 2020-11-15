import pyperclip

class User:
    """
    class that generates a new instance of a user
    """
    user_list=[] #empty user list

    def save_user(self):
        '''
        save user method saves user objects into user list
        '''
        User.user_list.append(self)


    def delete_user(self):
        '''
        delete_user method delete a saved used from user
        '''
        User.user_list.remove(self)

        

    def __init__(self,first_name,username,password,email):

        self.first_name=first_name
        self.username=username
        self.password=password
