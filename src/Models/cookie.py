import json

class Cookie:
    def __init__(self):
        pass

    def create(self):   #création d'un fichier json
        with open("cookie.json") as file:
            print("Fichier créé")

    def read(self):     #lecture d'un fichier json 
        with open("cookie.json", 'r') as file:
            return json.load(file)

    def write(self, dict):  #écrire dans un fichier json
        with open("cookie.json", 'w') as file:
            json.dump(dict, file)
    
    def update(self, data):     #modifier les valeurs attribuées aux clés
        c = self.read()
        for key in data.keys():
            c[key] = data[key]
        self.write(c)

    def clean(self, data):      #retirer les valeurs attribuées aux clés
        c = self.read()
        for key in data.keys():
            c[key] = None
        self.write(c)

    def drop(self):     #vider le fichier json
        self.write({})

