database_name = "lockerdatabase.db"

create_login_table_str = """ CREATE TABLE IF NOT EXISTS Login (
                                        id INTEGER PRIMARY KEY,
                                        username TEXT NOT NULL,
                                        password TEXT NOT NULL,
                                        date_logged_in TEXT NOT NULL
                                    ); """

check_if_table_exists_str = """SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Login' """

