import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import Image
from tkinter import PhotoImage

grap = tkinter.Tk()

grap.title("Themes")

style = ttk.Style()
style.configure("Monstyle.Tutton", foreground = "black", backgroud = "gray", font = ("Arial", 12, "bold"))


label = ttk.Label(grap, text="Nom: ", style= "Monstyle.TButton")
label.pack(pady=20)

button = ttk.Button(grap, text= "Bouton stylé", style= "Monstyle.TButton")
button.pack(pady = 10)

image = PhotoImage(file= "image.png")
Labimg = tkinter.Label(grap, image= image, width= 100, height= 100)
Labimg.pack(pady= 5)

grap.mainloop()