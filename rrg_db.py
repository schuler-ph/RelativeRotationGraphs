import mysql.connector
import json

class DatabaseManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="relativerotationgraphs"
        )
        self.cursor = self.conn.cursor()
        self.config = json.loads(open("config.json", "r").read())

    def drop_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS rrg_data")

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE rrg_data (
                symbol varchar(10) NOT NULL,
                date char(10) NOT NULL,
                value double(18,2) NOT NULL,
                PRIMARY KEY (date, symbol)
            )
        """)

    def insert_data(self, date, value, symbol):
        self.cursor.execute("INSERT INTO rrg_data (date, value, symbol) VALUES (%s, %s, %s)", (date, value, symbol))
        self.conn.commit()
