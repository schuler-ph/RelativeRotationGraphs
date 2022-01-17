import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="relativerotationgraphs"
        )
        self.cursor = self.db.cursor()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

    def insert_data(self, name, age):
        self.cursor.execute("INSERT INTO test_table (name, age) VALUES (%s, %s)", (name, age))
        self.db.commit()

    def select_data(self):
        self.cursor.execute("SELECT * FROM test_table")
        return self.cursor.fetchall()

    def delete_data(self, id):
        self.cursor.execute("DELETE FROM test_table WHERE id=%s", (id,))
        self.db.commit()

    def update_data(self, id, name, age):
        self.cursor.execute("UPDATE test_table SET name=%s, age=%s WHERE id=%s", (name, age, id))

    def close_connection(self):
        self.db.close()


if __name__ == "__main__":
    db = DatabaseManager()
    db.create_table()

    db.insert_data("John", 20)
    db.insert_data("Jane", 21)
    db.insert_data("Jack", 22)
    db.insert_data("Jill", 23)
    db.insert_data("Joe", 24)
    db.insert_data("Jenny", 25)
    db.insert_data("Juan", 26)

    print(db.select_data())

    db.delete_data(3)
    db.update_data(4, "Juanito", 27)

    print(db.select_data())

    db.close_connection()

    print("Done")


"""
    cnx = mysql.connector.connect(user='root', password='root',
                                host='localhost',
                                database='relativerotationgraphs')


    cursor = cnx.cursor()


    def get_all_tables():
        query = ("SELECT table_name FROM information_schema.tables "
                "WHERE table_schema = 'relativerotationgraphs'")
        cursor.execute(query)
        return cursor.fetchall()

    print(get_all_tables())

"""