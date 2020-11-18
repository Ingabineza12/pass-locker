import string
import random
global user_list

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
        self.email=email




class Credential:
    '''
    class of credential account, generate passwords information
    '''
    credential_list=[]
    user_credential_list=[]

    def __init__(self,first_name,site_name,account_name,password):
        '''
        Methode show the properties of user object
        '''
        self.first_name=first_name
        self.site_name=site_name
        self.account_name=account_name
        self.password=password


    def save_credential(self):
        '''
        methode to save credential globally
        '''

        Credential.credential_list.append(self)

    def generate_password(size=6, char=string.ascii_lowercase + string.ascii_uppercase+string.digits):
        '''
        method to generate random password
        '''
        generate=''.join(random.choice(char) for _ in range(size) )
        return generate

    @classmethod
    def check_user(cls,first_name,password):
        '''
        Method that checks if name and password enteries match
        '''
        current_user=''
        for user in User.user_list:
            if(user.first_name== first_name and user.password==password):
                current_user=user.first_name
        return current_user

    @classmethod
    def disp_credential(cls,first_name):
        '''
        method to display all list of saved credentials
        '''
        user_credential_list=[]
        for credential in cls.credential_list:
            if credential.first_name==first_name:
                user_credential_list.append(credential)
        return user_credential_list


    @classmethod
    def find_site(cls,site_name):
        '''
        Methode that find by site name and return credentials that match
        '''
        for credential in cls.credential_list:
            if credential.site_name==site_name:
                return credential
