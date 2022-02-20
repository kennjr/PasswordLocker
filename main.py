# This is a sample Python script.
import login2
import locker
import random, string


def login_interaction():
    while True:
        login_str = str(input("Login? [y/N] "))
        if login_str.lower() == "y":
            print("Name .........")
            name = str(input())
            code = generate_password()
            if code is not None:
                password = code
                print("Password .........")
                print(password)
            else:
                print("Password .........")
                password = str(input())
            login_attempt(name, password)
        elif login_str.lower() == "n":
            break


def login_attempt(name, password):
    user2 = login2.find_user(name)
    if user2 is not None:
        password_check = do_passwords_match(user2.password, password)
        if password_check:
            login2.update_current_user_val(user2)
            print(f"Welcome back {name}")
            locker_interaction()
        else:
            print("The name and password don't match. Please try again")
    else:
        new_user = login2.create_user(name, password)
        login2.save_user(new_user)
        login2.update_current_user_val(new_user)
        locker_interaction()


def locker_interaction():
    while True:
        print("""Use these codes to interact with passwordlocker - new-cred :to add new credentials
                                                               del-cred :to delete credentials
                                                               dis-cred :to display credentials
                                                               login :to login as diff. user""")
        action_str = str(input("")).lower()
        if action_str == 'new-cred':
            print("New Credentials")
            print("**"*10)

            print("Application/website .........")
            application = str(input())

            print("Username .........")
            username = str(input())

            # password = None
            code = generate_password()
            if code is not None:
                password = code
            else:
                print("Password .........")
                password = str(input())

            owner = login2.get_current_user_val()
            locker.add_credentials(locker.create_credential(application, username, password, owner.name))  # create and save new contact.
            print(f"The new credentials have been created: {application}, {username}, {password} for {owner.name}")
            print('\n')
            print(f"New Credentials for {application} created")
            print('\n')
        elif action_str == "dis-cred":
            owner = login2.get_current_user_val()
            cred_list = locker.get_all_credentials(owner.name)
            print(f"The owner is {owner.name}")
            if cred_list != []:
                print(f"""|Application || Username | Password|""")
                for credential in cred_list:
                    print(f"""|{credential.application} || {credential.username} | {credential.password}|""")
            else:
                print("You've not yet saved any credentials in locker")


def do_passwords_match(code_1, code_2):
    if code_1 == code_2:
        return True
    else:
        return False


def generate_password():
    code = None
    while True:
        print("Would you like a sys. generated password? [y/N] ")
        gen_code = str(input()).lower()
        if gen_code == "y":
            length = 10
            letters = string.ascii_lowercase
            code = ''.join(random.choice(letters) for i in range(length))
            break
        elif gen_code == "n":
            break
    return code

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # lockerdb.connect_to_db()
    print("Login to store and access auth credentials for other accounts")
    login_interaction()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
