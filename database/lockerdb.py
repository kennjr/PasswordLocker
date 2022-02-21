import sqlite3
import os
from constants import database_name
from constants import create_login_table_str
from constants import check_if_table_exists_str
import datetime

# Establish a connection to the Database and create
# a connection object
# If the file 'lockerdatabase.db' doesn't exist, the sys will create it for us
# The lockerdatabase.db is the db file
# conn = sqlite3.connect(database_name)


def check_db(filename):
    return os.path.exists(filename)


def connect_to_db():
    sqlite_connection = None
    try:
        sqlite_connection = create_connection(db_file=database_name)
        # Connect to DB and create a cursor
        cursor = sqlite_connection.cursor()
        print('DB Init')

        # Write a query and execute it with cursor
        query = 'select sqlite_version();'
        cursor.execute(query)

        # Fetch and output result
        result = cursor.fetchall()
        print('SQLite Version is {}'.format(result))

        # Close the cursor
        cursor.close()

    # Handle errors
    except sqlite3.Error as error:
        print('Error occurred - ', error)

    # Close DB Connection irrespective of success
    # or failure
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('SQLite Connection closed')


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn


def create_login_table(cursor):
    try:
            cursor.execute(create_login_table_str)
    except sqlite3.Error as e:
        print('Error occurred - ', e)


def check_if_table_exists(cursor, table_str):
    listOfTables = cursor.execute(check_if_table_exists_str).fetchone()

    # if the count is 1, then table exists
    if listOfTables[0] == 1:
        return True
    else:
        return True



def check_if_login_row_exists(cursor, username, table_str):
    cursor.execute(f"SELECT rowid FROM {table_str} WHERE username = ?", (username,))
    data = cursor.fetchone()

    if data is None:
        return None
    else:
        return data[0]


def check_db_connection_status(connection):
    if connection is not None:
        return True
    else:
        return False


def add_new_user(username, password):
    if username != "" and password != "":
        sqlite_connection = None
        try:
            sqlite_connection = create_connection(db_file=database_name)
            # Connect to DB and create a cursor
            cursor = sqlite_connection.cursor()
            create_login_table(cursor)
            if check_if_table_exists(cursor, "Login"):
                does_user_exist = check_if_login_row_exists(cursor, username, "Login")
                if does_user_exist is not None:
                    print(does_user_exist)
                else:
                    # using now() to get current time
                    current_time = datetime.datetime.now()
                    time_str = str(current_time)
                    insert_str = f'''INSERT INTO Login VALUES ({username}, {password}, {time_str})'''
                    # create the user row
                    add_data_to_table(cursor, insert_str)
            else:
                create_login_table(cursor)
                current_time = datetime.datetime.now()
                time_str = str(current_time)
                insert_str = f'''INSERT INTO Login VALUES ({username}, {password}, {time_str})'''
                # create the user row
                add_data_to_table(cursor, insert_str)
            # Close the cursor
            cursor.close()

        # Handle errors
        except sqlite3.Error as error:
            print('Error occurred - ', error)

        # Close DB Connection irrespective of success
        # or failure
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print('SQLite Connection closed')
    else:
        return


def add_data_to_table(cursor, insert_str):
    cursor.execute(insert_str)
