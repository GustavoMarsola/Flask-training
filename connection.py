from tinydb import TinyDB, Query

class Database:

    def __init__(self):
        self.db = TinyDB('db.json')
        self.user = Query()
    
    def compare(self, email,password):
        locate = self.db.search(self.user.email == email)
        if len(locate) == 0:
            print("Email não cadastrado")
            return False
        senha = locate[0]['senha']
        if senha != password:
            print("Senha incorreta")
            return False
        print("Login efetuado com sucesso")
        return True
