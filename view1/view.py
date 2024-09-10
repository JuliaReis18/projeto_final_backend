import tkinter as tk
from tkinter import messagebox

class UserView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Login e Cadastro - TwoWheel Tribe")

        # Cadastro
        self.lbl_email = tk.Label(self.root, text="E-mail")
        self.lbl_email.pack()
        self.entry_email = tk.Entry(self.root)
        self.entry_email.pack()

        self.lbl_password = tk.Label(self.root, text="Senha")
        self.lbl_password.pack()
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        self.btn_register = tk.Button(self.root, text="Cadastre-se", command=self.register)
        self.btn_register.pack()

        # Login
        self.btn_login = tk.Button(self.root, text="Login", command=self.login)
        self.btn_login.pack()

        self.root.mainloop()

    def register(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        success = self.controller.register_user(email, password)
        if success:
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Usuário já existe!")

    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        success = self.controller.login_user(email, password)
        if success:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")