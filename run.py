#!/usr/bin/env python3.6

from user import User
from user import Credential

def create_user(fname,name,pword,email):
    '''
    Function to create a new user account
    '''
    new_user = User(fname,name,pword,email)
    return new_user

def save_user(user):
    '''
    to save a new user account
    '''
    User.save_user(user)


def delete_user(user):
    '''
    function to delete a user
    '''
    user.delete_user()
def display_users():
    '''
    function to display all users
    '''
    return User.display_users()

def find_user(first_name):
    '''
    function that find user by the firstname
    '''
    return User.find_by_name(first_name)

def check_user(first_name,password):
    '''
    check if the account exist
    '''
    checking_user=Credential.check_user(first_name,password)
    return checking_user

def create_cred(first_name,site_name,account_name,password):
    '''
    new credential account
    '''
    new_credential=Credential(first_name,site_name,account_name,password)
    return new_credential

def save_credential(credential):
    '''
    to save all credentials
    '''
    Credential.save_credential(credential)
def delete_credential(credential):
    '''
    to save all credentials
    '''
    Credential.delete_credential(credential)

def disp_credential(first_name):
    '''
    to display all credentials stored
    '''
    return Credential.disp_credential(first_name)
def generate_password():
    '''
    function to give password randomly
    '''
    generate=Credential.generate_password()
    return generate

def copy_credential(site_name):
    '''
    function to copy credentials
    '''
    return Credential.copy_credential(site_name)
def check_existing_user(first_name):
        '''
        to check if the user exist
        '''
        return User.user_exist(first_name)

def main():
    print(' ')
    print('welcome to the password Locker application')
    while True:
        print(' ')
        print("*"*30)
        print("use these codes to navigate: \n ca - Create account \n li - Login \n du - Delete User \n dd - Dispaly all users \n ex - Exit")

        short_code = input('Please Enter your choice:').lower().strip()
        if short_code == 'ex':
            break
        elif short_code=='du':
            print("*"*30)
            print(' ')
            print("Delete a user----")
            search_email=input('Please Enter the first_name')
            if check_existing_user(search_email):
                search_user=find_user(search_email)
                print(f"{search_user.first_name} {search_user.username}")
                print("-"*20)
                print(f"Email.......{search_user.email}")
                print(f"FirstName...{search_user.first_name}")
                search_user.delete_user()
                print("User deleted!!!!!!")
            else:
                print("The user doesn't Exit")
        elif short_code=='dd' :
            print('*'*30)
            if display_users():
                print("List of all your Users")
                print('\n')
                for user in display_users():
                    print(f"{user.first_name} {user.username} {user.password} {user.email}")
                    print('\n')
            else:
                print('*'*30)
                print("you dont have any users saved ")


        elif short_code == 'ca':

            print("*"*30)
            print(' ')
            print("Create a new account:")
            first_name=input('Enter First_name: ').strip()
            username=input('Enter the Username: ').strip()
            password=input('Enter the Password: ').strip()
            email=input('Enter your Email: ').strip()
            save_user(create_user(first_name,username,password,email))
            print(" ")
            print(f'{first_name} {username} {email} {password} created successfully ')

        elif short_code == 'li':
            print("*"*30)
            print(' ')
            print("Login account:")

            first_name =input('Enter your Firstname: ').strip()
            password=str(input('Enter the Password: '))

            user_exists=check_user(first_name, password)
            if user_exists == first_name:
                print(" ")
                print(f'Welcome {first_name}.Please choose to continue.')
                print('')
                while True:
                    print("*"*30)
                    print('Navigation code: \n cc-Create a Credential \n dc-Display Credentials \n du - Delete Credential \n cp-Copy Password \n ex-Exit')
                    short_code=input('Please Enter your choice: ').lower().strip()
                    print("*"*30)
                    if short_code == 'ex':
                        print(" ")
                        print(f'Bye {first_name}')
                        break
                    elif short_code=='du':
                        print("*"*30)
                        print(' ')
                        print("Delete a Credential----")
                        print("Credential successfully deleted!!!!!!")
                        break
                        # search_email=input('Please Enter the first_name')
                        # if check_existing_user(search_email):
                        #     search_user=find_user(search_email)
                        #     print(f"{search_user.first_name} {search_user.username}")
                        #     print("-"*20)
                        #     print(f"Email.......{search_user.email}")
                        #     print(f"FirstName...{search_user.first_name}")
                        #     search_user.delete_credential()

                        # else:
                        #     print("The user doesn't Exit")
                    elif short_code =='cc':
                        print(' ')
                        print('Enter your credential: ')
                        site_name=input('enter the site name\'s name-').strip()
                        account_name=input('Enter your account\'s name- ').strip()
                        while True:
                            print(' ')
                            print("*"*30)
                            print('Please choose any option:\n ep-enter existing password \n ng-generate a password \n ex-exit')
                            passwor=input('Enter your option: ').lower().strip()
                            print("*"*30)
                            if passwor== 'ep':
                                print(" ")
                                password =input('Enter your password: ').strip()
                                break

                            elif passwor == 'ng':
                                password = generate_password()
                                print(f'Credential Created !!! Site Name: {site_name} -Account Name: {account_name} - Password: {password}')

                            elif passwor== 'ex':
                                break

                            else:
                                print('sorry!!! Wrong option and  Try again ')
                        save_credential(create_cred(first_name,site_name,account_name,password))
                        print(' ')
                        print(f'Credential Created !!! Site Name: {site_name} -Account Name: {account_name} - Password: {password}')
                        print('')
                    elif short_code == 'dc':
                        print(' ')
                        if disp_credential(first_name):
                            print('List of Credentials')
                            print(' ')
                            for credential in disp_credential(first_name):
                                print(f'Credential Created !!! Site Name: {site_name} -Account Name: {account_name} - Password: {password}')
                            print(' ')

                        else:
                                print(' ')
                                print(" you don't have any credential ")
                                print('')
                    elif short_code == 'cp':
                        print(' ')
                        chosen_site= input('Enter the site name to copy : ')
                        copy_credential(chosen_site)
                        print(' ')
                    else:
                        print('Wrong option!! Try again.')

            else:
                print(' ')
                print("try again or create an account")

        else:
            print("*"*30)
            print(' ')
            print(' Wrong option try Again.')




if __name__ == '__main__':
    main()
