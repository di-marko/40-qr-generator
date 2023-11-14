import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image, ImageTk
import qrcode
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

class App(ctk.CTk):
    def __init__(self):
        # Main window setup
        ctk.set_appearance_mode("light")
        super().__init__(fg_color="white")
        self.title_bar_style()
        
        # Customize the window
        self.title("QRGen") # Sets the title of the window as an empty string
        self.iconbitmap("img/logo.ico") # Sets the icon transparent
        self.geometry("400x400") # Set default window size
        
        # Input field
        self.input_string = ctk.StringVar()
        self.input_string.trace("w", self.create_qr)
        InputField(self, self.input_string, self.save_image)
        
        # Save button
        self.bind("<Return>", self.save_image)
        
        # QR code
        self.raw_image = None
        self.tk_image = None
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
            self.raw_image = None
            self.tk_image = None
            
    def save_image(self, event=""):
        if self.raw_image:
            file_path = filedialog.asksaveasfilename()
            
            if file_path:
                self.raw_image.save(file_path + ".png")
    
    def title_bar_style(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(0x00FFFFFF)), sizeof(c_int))
        except:
            pass
    
class InputField(ctk.CTkFrame):
    def __init__(self, parent, input_string, save_btn):
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
            command=save_btn, 
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