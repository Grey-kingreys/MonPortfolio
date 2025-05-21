import tkinter

#fonction
def recuperation():
    cadre2 = tkinter.LabelFrame(App, text="Recuperation", width = 600, height = 150)


    #creation et paramettrage des widget
    LabelNom = tkinter.Label(cadre2, text="Nom d'Utilisateur: ")
    EntryNom = tkinter.Entry(cadre2, textvariable = variableEntryNom.get())

    LabelMoDePass = tkinter.Label(cadre2, text="Mot de pass: ")
    EntryMoDePass = tkinter.Entry(cadre2, textvariable = VariableEntryMotDePass.get())



    #positionnement
    cadre2.grid(row=3, column = 0 )

    LabelNom.grid(row = 0, column = 0)
    EntryNom.grid(row = 0, column = 1)

    LabelMoDePass.grid(row = 1, column = 0)
    EntryMoDePass.grid(row = 1, column = 1)




App = tkinter.Tk()
App.title("Positionnement")
App.geometry("800x500")
cadre1 = tkinter.LabelFrame(App, width = 600, height = 150, border = 1, text= "Connexion")

#Variable
variableEntryNom = tkinter.StringVar()
VariableEntryMotDePass = tkinter.StringVar()
varshow = tkinter.StringVar()
varshow = "*"

#creation et paramettrage des widget
LabelNom = tkinter.Label(cadre1, text="Nom d'Utilisateur: ")
EntryNom = tkinter.Entry(cadre1, textvariable = variableEntryNom)
LabelMoDePass = tkinter.Label(cadre1, text="Mot de pass: ")
EntryMoDePass = tkinter.Entry(cadre1, textvariable = VariableEntryMotDePass, show = varshow )
valider = tkinter.Button(cadre1, text="Valider", command = recuperation)
annuler = tkinter.Button(cadre1, text="Annuler")



#positionnement
cadre1.grid(row = 0, column = 0)

LabelNom.grid(row = 0, column = 0)
EntryNom.grid(row = 0, column = 1)

LabelMoDePass.grid(row = 1, column = 0)
EntryMoDePass.grid(row = 1, column = 1)

valider.grid(row = 2, column=0)
annuler.grid(row = 2, column = 1)


App.mainloop()