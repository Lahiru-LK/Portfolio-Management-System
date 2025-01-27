#database.py
# database.py

import sqlite3

class PortfolioDatabase:
    def __init__(self, db_path="data/portfolio.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()
        self.db_path = db_path


    def get_all_securities(self):
        """
        Fetch all securities data from the database.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM securities")  # Assuming 'securities' table exists
        securities = cursor.fetchall()
        conn.close()
        return securities

    def get_security_by_id(self, sec_id):
        """
        Fetch a specific security by ID.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM securities WHERE id=?", (sec_id,))
        security = cursor.fetchone()
        conn.close()
        return security


    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS portfolio (
                id INTEGER PRIMARY KEY,
                type TEXT,
                name TEXT,
                ticker TEXT,
                price REAL,
                share REAL,
                sector TEXT,
                risk REAL
            )
        """)
        self.conn.commit()

    def add_security(self, security_type, name, ticker, price, share, sector, risk):
        self.cursor.execute("""
            INSERT INTO portfolio (type, name, ticker, price, share, sector, risk)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (security_type, name, ticker, price, share, sector, risk))
        self.conn.commit()

    def get_all_securities(self):
        self.cursor.execute("SELECT * FROM portfolio")
        return self.cursor.fetchall()

    def delete_by_id(self, row_id):
        try:
            self.cursor.execute("SELECT id FROM portfolio WHERE id = ?", (row_id,))
            result = self.cursor.fetchone()
            if not result:
                print(f"No security with ID {row_id} exists.")
                return False
            self.cursor.execute("DELETE FROM portfolio WHERE id = ?", (row_id,))
            self.conn.commit()
            print(f"Security with ID {row_id} has been successfully deleted.")
            return True
        except sqlite3.Error as e:
            print(f"Error deleting security: {e}")
            return False
