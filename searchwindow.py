from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QTextEdit
from PyQt5 import uic
from PyQt5.QtCore import Qt
import sqlite3

class Search_Window(QMainWindow):
    def __init__(self):
        super(Search_Window, self).__init__()

        #load UI File
        uic.loadUi('UI Files/searchwindow.ui', self)

        # define widgets
        self.search_lineEdit = self.findChild(QLineEdit,'search_lineEdit')

        self.result_text = self.findChild(QTextEdit,'textEdit')
        self.result_text.setReadOnly(True)                                    # read only
        self.result_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)   # show horiz scroll
        self.result_text.setLineWrapMode(QTextEdit.NoWrap)                    # no line wrap

        self.search_pushButton2 = self.findChild(QPushButton,'search_pushButton2')



        # connect button to its function
        self.search_pushButton2.clicked.connect(self.search)
        self.search_pushButton2.setDefault(True)
        self.search_lineEdit.returnPressed.connect(self.search)


#_____________________________________ define function________________________________________


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
                        result += f"\n                         === {table} ===\n"
                        for row in rows:
                            result += " , ".join(map(str, row)) + "\n"



                if not found:
                    self.result_text.setText(f"No matching records were found for '{keyword}'.")
                else:
                    self.result_text.setText(result)

        except Exception as e:
            self.result_text.setText(f"Error in search function : {e}")



