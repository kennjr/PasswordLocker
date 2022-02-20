# This is a sample Python script.
import login2


def login_interaction():
    while True:
        login_str = str(input("Login? [y/N] "))
        if login_str.lower() == "y":
            name = str(input("Name: "))
            password = str(input("Password: "))

            login2.save_user(login2.create_user(name, password))
            user2 = login2.find_user(name)
            login2.update_current_user_val(user2)
            print(login2.get_current_user_val().name)

            print(login2.check_for_existing_user(name))
            locker_interaction()
        elif login_str.lower() == "n":
            break


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

            # save_contact(create_contact(f_name, l_name, p_number, e_address))  # create and save new contact.
            print(f"The new credentials have been created: {application}, {username}, {password} for {owner.name}")
            print('\n')
            print(f"New Credentials for {application} created")
            print('\n')


def generate_password():
    code = None
    while True:
        print("Would you like a sys. generated password? [y/N] ")
        gen_code = str(input()).lower()
        if gen_code == "y":
            code = "passcode"
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
