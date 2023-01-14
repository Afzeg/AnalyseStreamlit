import sqlite3 

class Database:
    def __init__(self):
        self.db = sqlite3.connect("projet.db")
        self.execute = self.db.execute
        self.commit = self.db.commit

    def setup(self, mail, password):    
        self.execute("CREATE TABLE users (uid INTEGER PRIMARY KEY, mail VARCHAR, password VARCHAR)")
        self.execute(f"INSERT INTO users (mail, password) VALUES ('{mail}', '{password}')")
        self.commit()

    def drop(self):     #supprime la table
        self.execute("DROP TABLE IF EXISTS users")



