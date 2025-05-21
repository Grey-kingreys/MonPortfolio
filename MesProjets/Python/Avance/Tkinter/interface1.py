import tkinter
from tkinter import messagebox

def motDePass():
    app = tkinter.Tk()
    lab = tkinter.Label(app, text="saisissaiz votre mot de pass")
    sai = tkinter.Entry(app, width = 10, show="*")
    lab.pack()
    sai.pack()

def Erreur():
    messagebox.askretrycancel("Question", "Voulez vous continuer")



monapp = tkinter.Tk()
monapp.title("Ma premiere fênetre")

screenX = int(monapp.winfo_screenwidth())
screenY = int(monapp.winfo_screenheight())

windowX = 800
windowY = 500

posX = (screenX // 2) - (windowX // 2)
posY = (screenY // 2) - (windowY // 2)

geo = f"{windowX}x{windowY}+{posX}+{posY}"
monapp.geometry(geo)

malab = tkinter.Label(monapp, text = "Bonjour et Bienvenue dans mon application")
montext = tkinter.Entry(monapp, width = 30, )
button = tkinter.Button(monapp, text = "OK", command = motDePass)
boutton = tkinter.Checkbutton(monapp, text="Aime les pizza")
labelleRadio = tkinter.Label(monapp, text="As-tu faim?" )
radio1 = tkinter.Radiobutton(monapp, text="OUI", value="oui")
radio2 = tkinter.Radiobutton(monapp, text="NON", value="non")
curseur = tkinter.Spinbox(monapp, from_=10, to = 90)
Maliste = tkinter.Listbox(monapp)
Maliste.insert(1, "windows")
Maliste.insert(2, "MACBOOK")
Maliste.insert(3, "Linux")
buttonError = tkinter.Button(monapp, text = "Valider", command = Erreur)



malab.pack()
montext.pack()
button.pack()
boutton.pack()
labelleRadio.pack()
radio1.pack()
radio2.pack()
curseur.pack()
Maliste.pack()
buttonError.pack()

monapp.mainloop()