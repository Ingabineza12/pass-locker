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

    @classmethod
    def display_users(cls):
        '''
        method that display all user saved in the list
        '''
        return cls.user_list

     @classmethod
     def user_exist(cls,first_name):
        '''
        method that find by username and return all information that matches
        Args:
            name: first name to search for
        Returns:
            all information of that person
        '''
        for user in cls.user_list:
            if user.first_name== first_name:
                return True
        return False

    @classmethod
    def find_by_name(cls,first_name):
        '''
        method that find by username and return all information that matches
        Args:
            name: first name to search for
        Returns:
            all information of that person
        '''
        for user in cls.user_list:
            if user.first_name==first_name:
                return user


    def __init__(self,first_name,username,password,email):

        self.first_name=first_name
        self.username=username
        self.password=password
