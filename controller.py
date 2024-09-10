from model import UserModel
from view import UserView

class UserController:
    def __init__(self):
        self.model = UserModel()
        self.view = UserView(self)

    def register_user(self, username, password):
        return self.model.save_user(username, password)

    def login_user(self, username, password):
        return self.model.check_login(username, password)

if __name__ == "__main__":
    controller = UserController()