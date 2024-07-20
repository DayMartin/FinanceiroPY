import customtkinter
from db.consultas.user import *
# create_table()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class LoginComponent(customtkinter.CTkFrame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        texto = customtkinter.CTkLabel(self, text="Fazer Login")
        texto.pack(padx=10, pady=10)

        self.email_entry = customtkinter.CTkEntry(self, placeholder_text="Seu e-mail")
        self.email_entry.pack(padx=10, pady=10)

        self.senha_entry = customtkinter.CTkEntry(self, placeholder_text="Sua senha", show="*")
        self.senha_entry.pack(padx=10, pady=10)

        checkbox = customtkinter.CTkCheckBox(self, text="Lembrar Login")
        checkbox.pack(padx=10, pady=10)

        botao = customtkinter.CTkButton(self, text="Login", command=self.clique)
        botao.pack(padx=10, pady=10)

    def clique(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        if verificar_usuario(email, senha):
            self.controller.show_frame("HomeComponent")
        else:
            print("Nao login")
