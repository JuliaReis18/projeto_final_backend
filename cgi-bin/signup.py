import cgi
from controller1.main_controller import MainController

# Função para processar o cadastro
def handle_signup():
    form = cgi.FieldStorage()
    email = form.getvalue("email")
    senha = form.getvalue("senha")

    # Criar o controlador para processar
    controller = MainController()

    # Realizar o cadastro
    if controller.cadastrar_usuario(email, senha):
        print("Content-type:text/html\r\n\r\n")
        print("<html><body><h1>Cadastro realizado com sucesso!</h1></body></html>")
    else:
        print("Content-type:text/html\r\n\r\n")
        print("<html><body><h1>Usuário já existe!</h1></body></html>")

if __name__ == "__main__":
    handle_signup()