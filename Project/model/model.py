import sqlite3
from sqlite3 import IntegrityError
from pathlib import Path

cur_dir = Path.cwd()
db_dir = cur_dir.parent.joinpath("model", "database.db")


class Model:

    db = db_dir

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

    @classmethod
    def insert_page(cls, id, name):
        cls._create_pages_table()
        name = str(name).lower()
        with sqlite3.connect(cls.db) as conn:
            conn.cursor().execute("INSERT INTO pages(page_name,page_id) VALUES(?,?)",(name,id,))
            conn.commit()



    @classmethod
    def delete_page(cls, id):
        with sqlite3.connect(cls.db) as conn:
            conn.cursor().execute("DELETE FROM pages WHERE page_id = ?", (id,))
            conn.commit()


    @classmethod
    def get_page(cls, name=None, id=None):
        cls._create_pages_table()
        if id:
            with sqlite3.connect(cls.db) as conn:
                result = conn.cursor().execute("SELECT * FROM pages WHERE page_id = ?", (id,))
                return result.fetchone()
        if name:
            name = str(name).lower()
            with sqlite3.connect(cls.db) as conn:
                result = conn.cursor().execute("SELECT * FROM pages WHERE page_name LIKE ? ",(name[:6]+"%",))
                return result.fetchall()
        else:
            return cls.get_all()

    @classmethod
    def insert_user(cls,email,email_body):
        cls._create_user_table()
    ## DB holds only one record for the user. So we delete it everytime a new record is put
        with sqlite3.connect(cls.db) as conn:
            conn.cursor().execute("DELETE FROM user")
            conn.commit()
        with sqlite3.connect(cls.db) as conn:
            conn.cursor().execute("INSERT INTO user(email,email_body) VALUES(?,?)", (email, email_body,))
            conn.commit()

    @classmethod
    def get_user(cls):
        with sqlite3.connect(cls.db) as conn:
            result = conn.cursor().execute("SELECT * FROM user")
            res = result.fetchone()
            if len(res) > 0:
                return res
            else:
                return None



    @classmethod
    def get_all(cls):
        try:
            with sqlite3.connect(cls.db) as conn:
                result = conn.cursor().execute("SELECT * FROM pages")
                return result.fetchall()
        except:
            cls._create_pages_table()




if __name__ == "__main__":


    # Model.insert_page(1189230704429977, "DEV.bg")
    # Model.insert_page(140269359421625, "Nik")
    # Model.insert_page(181039705377403, "Sportvision")
    # result = Model.get_all()
    res= Model.get_user()
    print(res)
    # print(result)