
from src.Models.cookie import Cookie
from src.Models.database import Database
import re   #regular expressions
from hashlib import sha256

def valid_mail(mail):  #vérifie si le mail correspond bien aux normes qu'on demande
    regul = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    re.fullmatch(regul, mail)
    
    if re.fullmatch(regul, mail):
        return True
    else:
        return False

def valid_password(password):
    regul = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
    re.fullmatch(regul, password)

    if re.fullmatch(regul, password):
        return True
    else:
        return False

def login(mail, password):  #vérifie si le mail et le mdp sont dans la base de donnée users
    
    db = Database()
    password = sha256(str(password).encode(encoding="utf-32")).hexdigest()
    res = db.execute("SELECT * FROM users WHERE mail= (?) AND password= (?)", (mail, password)).fetchone()
    
    """
    a = set(db.execute(f"SELECT uid FROM users WHERE mail='{email}'").fetchall())
    b = set(db.execute("SELECT uid FROM users WHERE password='{mdp}'").fetchall())

    res = a.intersection(b)
    """
  
    if res != None:
        cook = Cookie()
        cook.update({'uid':res[0], 'mail':res[1]})
        return True
    else:
        return False


def open_access():
    c = Cookie()
    if c.read()["uid"] == None:
        return True
    else:
        return False
    
def logout():
    cook = Cookie()
    cook.clean({"uid":"", "mail":""})

def mail_exist(mail):
    db = Database()
    if db.execute(f"SELECT mail FROM users where mail ='{mail}'").fetchone() == None:
        return True
    else:
        return False

def signin(mail, mdp):
    db = Database()
    mdp = sha256(str(mdp).encode(encoding="utf-32")).hexdigest() 
    db.execute(f"INSERT INTO users (mail, password) VALUES ('{mail}','{mdp}')")
    db.commit()

