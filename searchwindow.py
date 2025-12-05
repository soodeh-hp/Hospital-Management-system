from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5 import uic
import sqlite3

class Search_Window(QMainWindow):
    def __init__(self):
        super(Search_Window, self).__init__()

        #load UI File
        uic.loadUi('searchwindow.ui', self)

        # define widgets
        self.search_lineEdit = self.findChild(QLineEdit,'search_lineEdit')
        self.result_label = self.findChild(QLabel,'result_label')
        self.search_pushButton2 = self.findChild(QPushButton,'search_pushButton2')

        # connect button to its function
        self.search_pushButton2.clicked.connect(self.search)


#______________________ define function________________________


    def search(self):
        keyword = self.search_lineEdit.text().strip()

        try:
            with sqlite3.connect("hospital.db") as conn:
                cursor = conn.cursor()

                # take all tables name
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                tables = [row[0] for row in cursor.fetchall()]

                result, found = "", False

                # Search each table
                for table in tables:
                    # take columns name
                    cursor.execute(f"PRAGMA table_info({table})")
                    columns = [col[1] for col in cursor.fetchall()]

                    # make search query
                    conditions = " OR ".join([f"{col} LIKE ?" for col in columns])
                    sql = f"SELECT * FROM {table} WHERE {conditions}"
                    params = [f"%{keyword}%"] * len(columns)

                    cursor.execute(sql, params)
                    rows = cursor.fetchall()

                    if rows:
                        found = True
                        result += f"\n=== {table} ===\n"
                        for row in rows:
                            result += " , ".join(map(str, row)) + "\n"



                if not found:
                    self.result_label.setText(f"No matching records were found for '{keyword}'.")
                else:
                    self.result_label.setText(result)

        except Exception as e:
            self.result_label.setText(f"Error in search function : {e}")



