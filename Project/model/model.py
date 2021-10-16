import sqlite3
from pathlib import Path

# Path to DataBase
cur_dir = Path.cwd()
db_dir = cur_dir.parent.joinpath("model", "database.db")


class Model:
    '''
     This is the class used for accessing and managing the DataBase. It uses  a sqlite database,
     which is quite sufficient for the scope of the app, especially when we have to package it for distribution.
     It's used for CRUD operations such as:
     -store, retrieve and delete facebook pages
     -store,retrieve and delete users
    '''

    db = db_dir

    # Using private methods for creating the databases. They are to be used only by the class itself(not outside of it)
    # so this encapsulates it to be used only by it's methods.#
    @classmethod
    def _create_pages_table(cls):
        with sqlite3.connect(cls.db) as conn:
            conn.cursor().execute("CREATE TABLE IF NOT EXISTS pages (id INTEGER PRIMARY KEY,"
                                  "page_name TEXT, page_id INTEGER type UNIQUE)")
            conn.commit()

    @classmethod
    def _create_user_table(cls):
        with sqlite3.connect(cls.db) as conn:
            conn.cursor().execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY,"
                                  "email TEXT, email_body TEXT)")
            conn.commit()

    # Class methods are being used instead of instance methods, because we're dealing with the class directly,
    # and there is only one variation of it, e.g no need to instantiate it to create different instances, that
    # have different properties (different settings) - at least this is not needed in this case.#

    @classmethod
    def insert_page(cls, id, name):
        cls._create_pages_table()
        name = str(name).lower()
        with sqlite3.connect(cls.db) as conn:
            conn.cursor().execute("INSERT INTO pages(page_name,page_id) VALUES(?,?)", (name, id,))
            conn.commit()

    @classmethod
    def get_page(cls, name=None, id=None):
        cls._create_pages_table()
        # Supporting search trough id or name of the FB page.
        if id:
            with sqlite3.connect(cls.db) as conn:
                result = conn.cursor().execute("SELECT * FROM pages WHERE page_id = ?", (id,))
                return result.fetchone()
        if name:
            name = str(name).lower()
            with sqlite3.connect(cls.db) as conn:
                result = conn.cursor().execute("SELECT * FROM pages WHERE page_name LIKE ? ", (name[:6] + "%",))
                return result.fetchall()
        # If nothing is specified get all the entries in the pages table.
        else:
            return cls.get_all()

    # Creating an explicit method for getting all entries from the pages table.
    @classmethod
    def get_all(cls):
        cls._create_pages_table()
        with sqlite3.connect(cls.db) as conn:
            result = conn.cursor().execute("SELECT * FROM pages")
            return result.fetchall()

    @classmethod
    def delete_page(cls, id):
        try:
            with sqlite3.connect(cls.db) as conn:
                conn.cursor().execute("DELETE FROM pages WHERE page_id = ?", (id,))
                conn.commit()
        except:
            return None

    @classmethod
    def delete_all(cls):
        try:
            with sqlite3.connect(cls.db) as conn:
                conn.cursor().execute("DELETE FROM pages")
                conn.commit()
        except:
            return None

    @classmethod
    def insert_user(cls, email, email_body):
        cls._create_user_table()
        # This table should hold only one record for the user. So we delete it everytime a new record is inserted
        with sqlite3.connect(cls.db) as conn:
            conn.cursor().execute("DELETE FROM user")
            conn.commit()
        with sqlite3.connect(cls.db) as conn:
            conn.cursor().execute("INSERT INTO user(email,email_body) VALUES(?,?)", (email, email_body,))
            conn.commit()

    @classmethod
    def get_user(cls):
        cls._create_user_table()
        try:
            with sqlite3.connect(cls.db) as conn:
                result = conn.cursor().execute("SELECT * FROM user")
                res = result.fetchone()
                if len(res) > 0:
                    return res
                else:
                    return None
        except:
            return None




if __name__ == "__main__":
    # Model.insert_page(1189230704429977, "DEV.bg")
    # Model.insert_page(140269359421625, "Nik")
    # Model.insert_page(181039705377403, "Sportvision")
    # result = Model.get_all()
    res = Model.get_user()
    print(res)
    # print(result)
