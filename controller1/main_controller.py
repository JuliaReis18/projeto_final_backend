
from model1.user_model import UserModel

class MainController:
    def __init__(self):
        self.user_model = UserModel()

    def cadastrar_usuario(self, email, senha):
        return self.user_model.save_user(email, senha)

    def fazer_login(self, email, senha):
        return self.user_model.check_login(email, senha)