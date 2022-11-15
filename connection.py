from tinydb import TinyDB, Query

class Database:

    def __init__(self):
        self.db = TinyDB('db.json')
        self.user = Query()
    
    def compare(self, email,password):
        locate = self.db.search(self.user.email == email)
        if len(locate) == 0:
            return "Email não cadastrado"
        senha = locate[0]['senha']
        if senha != password:
            return "Senha incorreta"
        return senha
