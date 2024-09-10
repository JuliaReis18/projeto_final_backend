import json
import os

class UserModel:
    def __init__(self, db_path="users.json"):
        self.db_path = db_path
        # Se o arquivo de usuários não existir, cria um novo.
        if not os.path.exists(self.db_path):
            with open(self.db_path, 'w') as file:
                json.dump({}, file)

    def save_user(self, username, password):
        users = self.load_users()
        if username in users:
            return False  # Usuário já existe
        users[username] = password
        with open(self.db_path, 'w') as file:
            json.dump(users, file)
        return True

    def load_users(self):
        with open(self.db_path, 'r') as file:
            return json.load(file)

    def check_login(self, username, password):
        users = self.load_users()
        return users.get(username) == password