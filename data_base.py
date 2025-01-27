import sqlite3




class Database:
    def __init__(self,path:str):
        self.path = path

    def create_table(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE  IF NOT EXISTS REVIEWS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            data INTEGER,
            phone_number TEXT,
            extra_comments TEXT
            )
            """)


            cursor.execute("""
             CREATE TABLE IF NOT EXISTS DISHES(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             price INTEGER,
             category TEXT,
             portion_option TEXT
             )
             """)

    def save_review(self,data:dict):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO reviews
                (name,data,phone_number,extra_comments)
                VALUES (?,?,?,?)
                """,
                (data["name"],data["date"],data["phone_number"],data["extra_comments"])
            )

    def save_dish(self, data: dict):
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                """
                    INSERT INTO dishes (name, price, category, portion_option)
                    VALUES (?, ?, ?, ?)
                """,
                    (data["name"], data["price"], data["category"], data["portion_option"])

                )

    def get_all_dishes(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            result = conn.execute("SELECT * FROM dishes")
            result.row_factory = sqlite3.Row
            data = result.fetchall()
            return [dict(row) for row in data]