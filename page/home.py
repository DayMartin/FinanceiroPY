import customtkinter
from menu import MenuComponent

class HomeComponent(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configurar o frame com a cor de fundo
        self.configure(fg_color='lightgray')
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Adicionar o menu
        menu = MenuComponent(parent=self, controller=controller)
        menu.grid(row=0, column=0, sticky="ew")

        # Adicionar conteúdo principal
        texto = customtkinter.CTkLabel(self, text="Home", font=("Arial", 24))
        texto.grid(row=1, column=0, padx=80, pady=80, sticky="nsew")

        # Ajustar o layout
        self.pack_propagate(False)
