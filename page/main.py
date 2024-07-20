import customtkinter
from menu import MenuComponent
from login import LoginComponent
from home import HomeComponent


class CustomFrame(customtkinter.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(fg_color='lightgray') 

class Application(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")

        self.frames = {}
        for F in (LoginComponent, MenuComponent, HomeComponent):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Configurar a distribuição do layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.show_frame("LoginComponent")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
