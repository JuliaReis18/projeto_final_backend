from model1.user_model import UserModel


if __name__ == "__main__":
    model = UserModel()  # Cria o modelo (e o arquivo users.json, se não existir)

    # Tenta cadastrar um novo usuário
    success = model.save_user("usuario@example.com", "minhasenha123")
    if success:
        print("Usuário cadastrado com sucesso!")
    else:
        print("Usuário já existe!")

    # Carrega todos os usuários cadastrados
    users = model.load_users()
    print("Usuários cadastrados:", users)