import customtkinter

class MenuComponent(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        clientes_button = customtkinter.CTkButton(self, text="Clientes", command=lambda: controller.show_frame("Clientes"))
        clientes_button.pack(side="left", padx=10, pady=10)

        fornecedores_button = customtkinter.CTkButton(self, text="Fornecedores", command=lambda: controller.show_frame("Fornecedores"))
        fornecedores_button.pack(side="left", padx=10, pady=10)

        produtos_button = customtkinter.CTkButton(self, text="Produtos", command=lambda: controller.show_frame("Produtos"))
        produtos_button.pack(side="left", padx=10, pady=10)

        vendas_button = customtkinter.CTkButton(self, text="Vendas", command=lambda: controller.show_frame("Vendas"))
        vendas_button.pack(side="left", padx=10, pady=10)

        compras_button = customtkinter.CTkButton(self, text="Compras", command=lambda: controller.show_frame("Compras"))
        compras_button.pack(side="left", padx=10, pady=10)

        financeiro_button = customtkinter.CTkButton(self, text="Financeiro", command=lambda: controller.show_frame("Financeiro"))
        financeiro_button.pack(side="left", padx=10, pady=10)
