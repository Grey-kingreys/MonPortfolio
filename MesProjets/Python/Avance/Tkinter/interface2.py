import tkinter
from tkinter import messagebox

def observeEntry(*args):
    varlabEnt.set(varEnt.get())

def buttonEntry():
    messagebox.showerror("Erreur", varEnt.get())
    

def observeCk(*args):
    varlabCh.set(varCh.get())

def observeRadio(*args):
    varLabRad.set(varRadio.get())

App = tkinter.Tk()
App.geometry("500x300")

varlabEnt = tkinter.StringVar()
varEnt = tkinter.StringVar()

varCh = tkinter.StringVar()
varlabCh = tkinter.StringVar()

varRadio = tkinter.IntVar()
varLabRad = tkinter.IntVar()

varEnt.trace("w", observeEntry)
varCh.trace("w", observeCk)
varRadio.trace("w", observeRadio)

lablEnt = tkinter.Label(App, text="", textvariable = varlabEnt)
saisi = tkinter.Entry(App, textvariable = varEnt, )
buttonEn = tkinter.Button(App, text="OK", command = buttonEntry)

labelck = tkinter.Label(App, text="", textvariable = varlabCh)
coche = tkinter.Checkbutton(App, text="PIZZA", onvalue = "OUI", offvalue = "NON", variable = varCh)

rad1 = tkinter.Radiobutton(App, text = "Oui", value=1, variable = varRadio)
rad2 = tkinter.Radiobutton(App, text = "Non", value=2, variable = varRadio)
labRadio = tkinter.Label(App, text="", textvariable = varLabRad)




lablEnt.pack()
saisi.pack()
buttonEn.pack()
coche.pack()
labelck.pack()
rad1.pack()
rad2.pack()
labRadio.pack()
App.mainloop()