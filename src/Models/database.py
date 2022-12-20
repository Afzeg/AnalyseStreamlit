import sqlite3 

class Database:
    def __init__(self):
        self.db = sqlite3.connect("projet.db")
        self.execute = self.db.execute
        self.commit = self.db.commit

    def setup(self):    
        self.execute("CREATE TABLE users (uid INTEGER PRIMARY KEY, mail VARCHAR, password VARCHAR)")
        self.execute("INSERT INTO users (mail, password) VALUES ('erwan@mail.fr', '932a8e294c3c14a0f47ad4df4890bf25b034038ba88fe9fddf4b727076cc12ef')")
        self.commit()

    def drop(self):     #supprime la table
        self.execute("DROP TABLE IF EXISTS users")



#db = Database().setup()

"""
d.execute("CREATE TABLE users (uid INTEGER PRIMARY KEY UNIQUE, mail VARCHAR, password VARCHAR)")
a = d.execute("INSERT INTO users(mail, password) VALUES ('erwan@mail.fr', '123456789')").fetchall()
print(a)
"""

