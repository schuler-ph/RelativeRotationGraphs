import mysql.connector
import json


class DatabaseManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="relativerotationgraphs",
        )
        self.cursor = self.conn.cursor()

    def get_config(self):
        return json.loads(open("src/config.json", "r").read())

    def drop_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS rrg_data")

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE rrg_data (
                symbol varchar(10) NOT NULL,
                date char(10) NOT NULL,
                value double(18,2) NOT NULL,

                price_relative double(18,2) NULL,

                rs_ratio double(18,2) NULL,
                rs_ratio_avg double(18,2) NULL,
                rs_momentum double(18,2) NULL,
                rs_momentum_avg double(18,2) NULL,

                PRIMARY KEY (date, symbol)
            )
        """
        )

    def commit(self):
        self.conn.commit()

    def get_data(self, symbol):
        self.cursor.execute(
            "SELECT * FROM rrg_data WHERE symbol = %s ORDER BY date DESC", (symbol,)
        )
        return self.cursor.fetchall()

    def insert_value(self, symbol, date, value):
        self.cursor.execute(
            "INSERT INTO rrg_data (symbol, date, value) VALUES (%s, %s, %s)",
            (symbol, date, value),
        )

    def insert_price_relative(self, symbol, date, value):
        self.cursor.execute(
            "UPDATE rrg_data SET price_relative = %s WHERE symbol = %s AND date = %s",
            (value, symbol, date),
        )

    def insert_rs_ratio(self, symbol, date, value):
        self.cursor.execute(
            "UPDATE rrg_data SET rs_ratio = %s WHERE symbol = %s AND date = %s",
            (value, symbol, date),
        )

    def insert_rs_ratio_avg(self, symbol, date, value):
        self.cursor.execute(
            "UPDATE rrg_data SET rs_ratio_avg = %s WHERE symbol = %s AND date = %s",
            (value, symbol, date),
        )

    def insert_rs_momentum(self, symbol, date, value):
        self.cursor.execute(
            "UPDATE rrg_data SET rs_momentum = %s WHERE symbol = %s AND date = %s",
            (value, symbol, date),
        )

    def insert_rs_momentum_avg(self, symbol, date, value):
        self.cursor.execute(
            "UPDATE rrg_data SET rs_momentum_avg = %s WHERE symbol = %s AND date = %s",
            (value, symbol, date),
        )
