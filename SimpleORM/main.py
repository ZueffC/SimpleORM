from sqlite3 import *


class DB():
    def __init__(self, name):
        self.name = name
   
    def connect(self):
        self.connection = connect(self.name)
        self.cursor = self.connection.cursor()
    
    def readData(self, selected_fields, name):
        text = f"SELECT {selected_fields} FROM {name};"
        text = str(text)
        #Adding command to execute
        self.cursor.execute(text)
        results = self.cursor.fetchall()
        return results
    
    def addData(self, name, values):
        text = f"INSERT INTO {name} VALUES ({values});"
        text = str(text)
        #Adding command to execute
        self.cursor.execute(text)
        self.connection.commit()

    def createTable(self, name, fields):
        text = f"CREATE TABLE IF NOT EXISTS {name} ({fields});"
        text = str(text)
        #Adding command to execute
        self.cursor.execute(text)
        self.connection.commit()
    
    