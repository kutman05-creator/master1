import sqlite3

from handlers.review_dialog import extra_process


class Database:
    def __init__(self,path:str):
        self.path = path

    def create_table(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS REVIEWS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            data INTEGER,
            phone_number TEXT,
            extra_comments TEXT
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
                (data["name"],data["data"],data["phone_number"],data["extra_comments"])
            )
