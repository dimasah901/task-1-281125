import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QWidget, QApplication, QLabel, QTableWidgetItem)
from main_ui import Ui_Form
from sqlite3 import Connection

class Car(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connection = Connection("coffee.sqlite")
        self.connection.autocommit = True
        self.connection.cursor().execute("""
            CREATE TABLE IF NOT EXISTS coffee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sort TEXT,
                rarity TEXT,
                state TEXT,
                taste TEXT,
                price TEXT,
                volume TEXT
            )
        """).fetchall()
        self.data = self.connection.cursor().execute("SELECT * FROM coffee").fetchall()
        self.ui.tableWidget.setRowCount(len(self.data))
        for i, row in enumerate(self.data):
            for j, item in enumerate(row):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(item))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Car()
    ex.show()
    sys.exit(app.exec())
