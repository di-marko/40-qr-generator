import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import qrcode

class App(ctk.CTk):
    def __init__(self):
        # Main window setup
        ctk.set_appearance_mode("light")
        super().__init__(fg_color="white")
        
        # Customize the window
        self.title("") # Sets the title of the window as an empty string
        self.iconbitmap("empty.ico") # Sets the icon transparent
        self.geometry("400x400") # Set default window size
        
        # Input field
        self.input_string = ctk.StringVar()
        self.input_string.trace("w", self.create_qr)
        InputField(self, self.input_string)
        
        # QR code
        self.qr_image = QRCodeImage(self)
        
        # Run the app
        self.mainloop()
        
    def create_qr(self, *args):
        current_text = self.input_string.get()
        if current_text:
            self.raw_image = qrcode.make(current_text).resize((300,300))
            self.tk_image = ImageTk.PhotoImage(self.raw_image)
            self.qr_image.update_image(self.tk_image)
        else:
            self.qr_image.clear()
        
class InputField(ctk.CTkFrame):
    def __init__(self, parent, input_string):
        super().__init__(master=parent, corner_radius=0, fg_color="#1C1C1C")
        self.place(relx=0.5, rely=1, relwidth=1, relheight=0.4, anchor="center")
        
        # Create grid layout
        self.rowconfigure((0,1), weight=1, uniform="a")
        self.columnconfigure(0, weight=1, uniform="a")
        
        # Create the input widgets
        self.frame = ctk.CTkFrame(self, fg_color="transparent")
        self.frame.columnconfigure(0, weight=1, uniform="b")
        self.frame.columnconfigure(1, weight=4, uniform="b")
        self.frame.columnconfigure(2, weight=2, uniform="b")
        self.frame.columnconfigure(3, weight=1, uniform="b")
        self.frame.grid(row=0, column=0)
        
        input_field = ctk.CTkEntry(
            self.frame, 
            textvariable=input_string, 
            fg_color="#fff", 
            text_color="#1C1C1C", 
            corner_radius=0, 
            border_width=0)
        input_field.grid(row=0, column=1, sticky="nsew")
        
        button = ctk.CTkButton(
            self.frame, 
            text="Save QR", 
            fg_color="#fff", 
            text_color="#1C1C1C", 
            corner_radius=0, 
            hover_color="#f1f1f1")
        button.grid(row=0, column=2, sticky="nsew", padx=12)
        
class QRCodeImage(tk.Canvas):
    def __init__(self, parent):
        super().__init__(
            master=parent, 
            background="#fff", 
            bd=0, 
            highlightthickness=0, 
            relief="ridge")
        self.place(relx=0.5, rely=0.4, width=300, height=300, anchor="center")
        
    def update_image(self, image_tk):
        self.clear()
        self.create_image(0,0, image = image_tk, anchor="nw")
        
    def clear(self):
        self.delete("all")
        
App()