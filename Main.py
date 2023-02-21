from Utils import *
from TinyRC4 import *

from tkinter import *
import customtkinter


def returnPressed(event):
    print("test")

def button_event(entry1, entry3):
    # xoa du lieu cu
    du_lieu.clear()

    e1 = entry1.get()
    e3 = entry3.get()
    binary = 0

    try:
        # e3 = str(e3).replace(" ", "")
        # e3 = str(e3).split(",")
        e3 = [int(x) for a,x in enumerate(str(e3))]

        # xu ly du lieu
        for i in range(len(e3)):
            e3[i] = int(e3[i])
        binary = TextToDecimal(e1)

        # ma hoa
        rc4 = TinyRC4()
        result = rc4.encrypt_int(binary, len(e1), e3)
        du_lieu["---------------"] = ""
        du_lieu["Kết quả"] = ""
        du_lieu["dữ liệu được mã hoá (dang binary) "] = DecimalToBinaryWithPlainText(result, len(e1))
        du_lieu["dữ liệu được mã hoá (dang chu) "] = BinaryToText(DecimalToBinaryWithPlainText(result, len(e1)))
        app.refresh()

    except:
        error = customtkinter.CTkToplevel()
        error.geometry("200x100")
        error.title("error")
        label = customtkinter.CTkLabel(master=error, text="du lieu sai", text_color="red")
        label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        error.focus()
    




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(1, weight=1)
        self.geometry("370x500")
        self.minsize(370, 500)
        self.title("tinyRC4")

        label = customtkinter.CTkLabel(master=self, text="tinyRC4", font=("", 30))
        label.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        entry1 = customtkinter.CTkEntry(master=self, placeholder_text="Dữ liệu \n(chỉ nhập từ A-H)")
        entry1.grid(row=1, column=1, padx=25, pady=5, sticky="nsew")
        entry3 = customtkinter.CTkEntry(master=self, placeholder_text="Khoá")
        entry3.grid(row=2, column=1, padx=25, pady=5, sticky="nsew")

        label1 = customtkinter.CTkLabel(master=self, text="Dữ liệu \n(chỉ nhập từ A-H)")
        label1.grid(row=1, column=0, padx=10, pady=5)
        label3 = customtkinter.CTkLabel(master=self, text="Khoá")
        label3.grid(row=2, column=0, padx=10, pady=5)

        button = customtkinter.CTkButton(master=self, text="Mã hoá/Giải mã", command=lambda : button_event(entry1, entry3))
        button.grid(row=3, column=0, padx=15, pady=15, columnspan=2)
        self.bind('<Return>', lambda event : button_event(entry1, entry3))
    
        self.textbox = customtkinter.CTkTextbox(master=self, width=300, height=200, corner_radius=10)
        self.textbox.grid(row=4, column=0, sticky="nsew", padx=15, pady=15, columnspan=2)
        self.textbox.configure(state = "disabled")

    def refresh(self):
        self.textbox.configure(state = "normal")
        self.textbox.delete('1.0', END)
        for i in (du_lieu):
            self.textbox.insert("50.0", str(i) + ": " + str(du_lieu[i]) + "\n")
        self.textbox.configure(state = "disabled")



if __name__ == '__main__':
    app = App()
    app.mainloop()