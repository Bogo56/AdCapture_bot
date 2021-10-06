import sqlite3
from sqlite3 import IntegrityError



class Model:

    db = "D:\Programming\Work_Projects\ScreenShotApp(new)\Project\model\database.db"

    @classmethod
    def _create_table(cls):
        with sqlite3.connect(cls.db) as conn:
            conn.cursor().execute("CREATE TABLE IF NOT EXISTS pages (id INTEGER PRIMARY KEY,"
                            "page_name TEXT, page_id INTEGER type UNIQUE)")
            conn.commit()


    @classmethod
    def insert_page(cls, id, name):
        cls._create_table()
        name = str(name).lower()
        try:
            with sqlite3.connect(cls.db) as conn:
                conn.cursor().execute("INSERT INTO pages(page_name,page_id) VALUES(?,?)",(name,id,))
                conn.commit()
        except IntegrityError:
            return "Page is already in the database"


    @classmethod
    def delete_page(cls, id):
        with sqlite3.connect(cls.db) as conn:
            conn.cursor().execute("DELETE FROM pages WHERE page_id = ?", (id,))
            conn.commit()


    @classmethod
    def get_page(cls, name=None, id=None):
        cls._create_table()
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
    def get_all(cls):
        try:
            with sqlite3.connect(cls.db) as conn:
                result = conn.cursor().execute("SELECT * FROM pages")
                return result.fetchall()
        except:
            cls._create_table()




if __name__ == "__main__":


    # Model.insert_page(1189230704429977, "DEV.bg")
    # Model.insert_page(140269359421625, "Nik")
    Model.insert_page(181039705377403, "Sportvision")
    result = Model.get_all()
    print(result)
