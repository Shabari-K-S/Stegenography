import customtkinter as ctk 
from PIL import ImageTk, Image
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Custom Tkinter")
        self.geometry("500x300")
        self.resizable(False, False)

        main_frame = ctk.CTkFrame(self, width=490, height=290)
        main_frame.grid(row=0, column=0, padx=5, pady=5)

        logo = ctk.CTkImage(Image.open("images/modifiedlogo.png"), size=(410, 65))
        logo_label = ctk.CTkLabel(main_frame, image=logo,text='')
        logo_label.grid(row=0, column=0, padx=40, pady=40, columnspan=2)

        title_label = ctk.CTkLabel(main_frame, text="Data Hider inside an image", font=("consolas", 30))
        title_label.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

        opt_label = ctk.CTkLabel(main_frame, text="Select an option", font=("consolas", 20))
        opt_label.grid(row=2, column=0, padx=10, pady=5, columnspan=2)

        btn = ctk.CTkButton(main_frame, text="Text Inside JPEG", command=self.text_inside_jpeg)
        btn.grid(row=3, column=0, padx=5, pady=10,columnspan=2)



    def text_inside_jpeg(self):
        tij = ctk.CTkToplevel(self)
        tij.title("Text Inside JPEG")
        tij.geometry('1200x700')
        tij.grab_set()

        head = ctk.CTkLabel(tij, text="Steganography - Hide Data in a Image File", font=("consolas", 30))
        head.grid(row=0, column=0, columnspan=2, padx=10,pady=10)

        frame = ctk.CTkFrame(tij, width=1180, height=600)
        frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        frame_img = ctk.CTkFrame(frame, width=900, height=580)
        frame_img.grid(row=0, column=0, padx=5, pady=10)

        frame_opt = ctk.CTkFrame(frame, width=270, height=580)
        frame_opt.grid(row=0, column=1, padx=5, pady=10)

        
        self.img_label = ctk.CTkLabel(frame_img, text="Select an JPEG image",width=840, height=580,font=("consolas", 20))
        self.img_label.grid(row=0, column=0)

        label_1 = ctk.CTkLabel(frame_opt, text="Select your Image:", font=("consolas", 16))
        label_1.grid(row=0, column=0, padx=10, pady=10)
        
        btn = ctk.CTkButton(frame_opt, text="Click", command=self.select_image)
        btn.grid(row=0, column=1, padx=5, pady=10)

        self.secret = ctk.CTkTextbox(frame_opt, width=300,height=390 ,font=("consolas", 16))
        self.secret.grid(row=2, column=0,padx=5, pady=10, columnspan=2)

        btn = ctk.CTkButton(frame_opt, text="Hide", command=self.hide)
        btn.grid(row=3, column=0, padx=5, pady=10)

        btn = ctk.CTkButton(frame_opt, text="Reveal", command=self.reveal)
        btn.grid(row=3, column=1, padx=5, pady=10)

        save = ctk.CTkButton(frame_opt, text="About Us", command=self.save)
        save.grid(row=4, column=0, padx=5, pady=20, columnspan=2)





    def select_image(self):
        self.img = ctk.filedialog.askopenfile(mode='r',filetypes=[('JPEG File', '*.jpeg'),('PNG File', '*.png')])
        self.image = ImageTk.PhotoImage(Image.open(self.img.name))

        self.img_label.configure(image=self.image,text="",width=840,height=580)

        loc = os.path.split(self.img.name)

        self.img_location = loc[0]

        print(self.img_location)

    def hide(self):
        with open(self.img.name, "rb") as f, open(self.img_location+"/encrypted_img.jpeg", "wb") as f2:
            if len(self.secret.get("1.0",ctk.END)) > 1:
                print(len(self.secret.get("1.0",ctk.END)))
                f2.write(f.read())

                f2.write(bytes(self.secret.get("1.0",ctk.END), encoding='utf-8'))


            else:
                error_secret = ctk.CTkToplevel(self)
                error_secret.title("Error")
                error_secret.geometry('350x120')
                error_secret.grab_set()

                error_label = ctk.CTkLabel(error_secret, text="Please enter a secret message", font=("consolas", 16))
                error_label.grid(row=0,column=0,pady=10,padx=35,columnspan=2)
    def reveal(self):
        with open(self.img.name, "rb") as f:
            content = f.read()
            offset = content.index(bytes.fromhex('FFD9'))

            f.seek(offset+2)
            print(decoded_value:=f.read().decode())

            new_window = ctk.CTkToplevel(self)
            new_window.title("Decrypted Data")
            new_window.geometry('350x155')
            new_window.grab_set()

            new_label = ctk.CTkLabel(new_window, text=decoded_value, font=("consolas", 16))
            new_label.grid(row=0,column=0,pady=10,padx=35,columnspan=2)

    def save(self):
        print("About US")

app = App()
app.mainloop()
