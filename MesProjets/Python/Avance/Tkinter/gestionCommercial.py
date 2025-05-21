#Ce projet consiste a creer une application de gestion commercial
import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import Image
from tkinter import PhotoImage




#Les fonction

#Connexion
def Connexion():
    connexion = tkinter.Toplevel(GC)
    connexion.title("Connexion")
    screen_x = int(connexion.winfo_screenwidth())
    screen_y = int(connexion.winfo_screenheight())

    window_x = 500
    window_y = 200

    pos_x = (screen_x // 2) - (window_x // 2)
    pos_y = (screen_y // 2) - (window_y // 2)
    geo = f"{window_x}x{window_y}+{pos_x}+{pos_y}"
    connexion.geometry(geo)
    cadreconn = ttk.LabelFrame(connexion, width = 400, height = 180, text = "Connexion", style="Monstyle.TButton")

    Identifiant = ttk.Label(cadreconn, text="Identifiant", style= "Monstyle.TButton")
    ChampsId = tkinter.Entry(cadreconn)

    Motdepass = tkinter.Label(cadreconn, text = "Mot de pass")
    ChampsMDP = tkinter.Entry(cadreconn)
    
    Valider = tkinter.Button(cadreconn, text="Valider")
    Annuler = tkinter.Button(cadreconn, text="Annuler")

    cadreconn.pack(side = "right")
    Identifiant.grid(row = 0, column = 0)
    ChampsId.grid(row = 0, column = 1)
    Motdepass.grid(row = 1, column = 0)
    ChampsMDP.grid(row = 1, column = 1)
    Valider.grid(row= 2, column= 0)
    Annuler.grid(row=2, column=1)
    
    
#Ajouter une nouvelle categorie
def newCategorie():
    newCategorie = tkinter.Toplevel(GC)
    newCategorie.title("Nouvelle Categorie")
    screen_x = int(newCategorie.winfo_screenwidth())
    screen_y = int(newCategorie.winfo_screenheight())
    
    window_x = 600
    window_y = 170
    
    pos_x = (screen_x // 2) - (window_x // 2)
    pos_y = (screen_y // 2) - (window_y // 2)
    
    pos = f"{window_x}x{window_y}+{pos_x}+{pos_y}"
    newCategorie.geometry(pos)
    cadre = tkinter.LabelFrame(newCategorie, text= "Nouvelle Categorie", width= 550, height= 250)
    cadrehaut1 = tkinter.Frame(cadre, width= 100, height= 50)
    cadrehaut2 = tkinter.Frame(cadre, width= 100 , height=50)
    
    
    IdCategorie = tkinter.Label(cadre, text= "ID Categorie", state= "disabled")
    IDEcategorie = tkinter.Entry(cadre, state= "disabled")
    NomCategorie = tkinter.Label(cadre, text="Nom Categorie")
    EntryCategorie = tkinter.Entry(cadre)
    Valider = tkinter.Button(cadre, text= "Valider", width= 10)
    Annuler = tkinter.Button(cadre, text= "Annuler", width= 10)
    
    
    
    cadreC = tkinter.Frame(cadre, width=100, height= 50)
    cadreBas = tkinter.Frame(cadre, width= 100, height=50)
    
    
    cadre.pack()
    cadrehaut1.grid(row=0, column = 0)
    cadrehaut2.grid(row = 0, column= 1)
    
    IdCategorie.grid(row= 1, column= 0)
    IDEcategorie.grid(row=1, column= 1)
    NomCategorie.grid(row=2, column=0)
    EntryCategorie.grid(row=2, column= 1)
    Valider.grid(row=2, column=2)
    Annuler.grid(row= 2, column= 3)
    
    cadreBas.grid(row=3, column= 0, rowspan= 2)
    
    
#Liste des categorie
def ListeCategorie():
    ListeCategorie = tkinter.Toplevel(GC)
    ListeCategorie.title("Liste Des Categorie")
    screen_x = int(ListeCategorie.winfo_screenwidth())
    screen_y = int(ListeCategorie.winfo_screenheight())

    window_x = 1000
    window_y = 600

    pos_x = (screen_x // 2) - (window_x // 2)
    pos_y = (screen_y // 2) - (window_y // 2)
    geo = f"{window_x}x{window_y}+{pos_x}+{pos_y}"
    ListeCategorie.geometry(geo)
    
    #Creation du tableau
    
    tableCategorie = ttk.Treeview(ListeCategorie)
    tableCategorie["columns"] = ("IDCategorie")
    
    #config des colonne
    
    tableCategorie.column("#0", width=120, minwidth= 50)
    tableCategorie.column("IDCategorie", width=500)
    
    #Ajout des Entete
    tableCategorie.heading("#0", text="ID Categorie")
    tableCategorie.heading("#1", text="Nom des Categorie")
    


    tableCategorie.pack()
    
    
#Ajouter un produit

def AjouterProduit():
    nouveauProduit = tkinter.Toplevel(GC)
    nouveauProduit.title("Nouveau Produit")
    screen_x = int(nouveauProduit.winfo_screenwidth())
    screen_y = int(nouveauProduit.winfo_screenheight())
    
    window_x = 600
    window_y = 300
    
    pos_x = (screen_x // 2) - (window_x // 2)
    pos_y = (screen_y // 2) - (window_y // 2)
    
    pos = f"{window_x}x{window_y}+{pos_x}+{pos_y}"
    nouveauProduit.geometry(pos)
    
    cadre = tkinter.LabelFrame(nouveauProduit, width= 550, height= 250, highlightbackground= "red", text= "Ajouter un Produit")
    Nomproduit = ttk.Label(cadre, text= "NomProduit", style= "Monstyle.TButton", width= 15)
    EntrerNomProduit = ttk.Entry(cadre, style= "Monstyle.TButton")
    Descproduit = ttk.Label(cadre, text= "DescriptionProduit", style = "Monstyle.TButton", width= 15)
    EntryDescProduit = ttk.Entry(cadre, style= "Monstre.TButton")
    prixProduit = ttk.Label(cadre, text="PrixProduit", style = "Monstyle.TButton", width= 15)
    EntryPrixProduit = ttk.Entry(cadre, style = "Monstyle.TButton")
    Categorie = ttk.Label(cadre, text= "Categorie", style = "Monstyle.TButton", width= 15)
    comboCategorie = ttk.Combobox(cadre, style = "Monstyle.TButton")
    imageprod = ttk.Entry(cadre, )
    
    
    
    cadre.grid(row=1, column=1, padx= 5, pady=5)
    Nomproduit.grid(row=0, column= 0)
    EntrerNomProduit.grid(row= 0, column= 1)
    Descproduit.grid(row=1, column=0)
    EntryDescProduit.grid(row=1, column=1)
    prixProduit.grid(row= 2, column= 0)
    EntryPrixProduit.grid(row= 2, column= 1)
    Categorie.grid(row= 3, column= 0)
    comboCategorie.grid(row=3 , column= 1)
    

#Liste des produit
def ListeProduit():
    ListeProduit = tkinter.Toplevel(GC)
    ListeProduit.title("Liste Des Produits")
    screen_x = int(ListeProduit.winfo_screenwidth())
    screen_y = int(ListeProduit.winfo_screenheight())

    window_x = 1000
    window_y = 600

    pos_x = (screen_x // 2) - (window_x // 2)
    pos_y = (screen_y // 2) - (window_y // 2)
    geo = f"{window_x}x{window_y}+{pos_x}+{pos_y}"
    ListeProduit.geometry(geo)
    
    #ajout du tableau
    
    tableProduit = ttk.Treeview(ListeProduit)
    tableProduit["columns"] = ("Nom", "age", "Profession")
    
    #configuration des colonne
    
    
    
    tableProduit.pack()
    
#Creation de la fenetre principale
GC = tkinter.Tk()
screen_x = int(GC.winfo_screenwidth())
screen_y = int(GC.winfo_screenheight())

window_x = 1024
window_y = 600

pos_x = (screen_x // 2) - (window_x // 2)
pos_y = (screen_y // 2) - (window_y // 2)
geo = f"{window_x}x{window_y}+{pos_x}+{pos_y}"
GC.geometry(geo)

GC.title("Gestionnaire Des Produits")

#Creation et configuration du style

style1 = ttk.Style()
style1.configure("Monstyle.TButton", foreground = "black", backgroud = "gray", font = ("Arial", 12, "normal"))
style2 = ttk.Style()
style2.theme_use("vista")

#Creation du barre du menu
BarreMenue = tkinter.Menu(GC, title="Menu Principale", font= ("Times New Roman", 12))



#Creation des Menue secondaire et leurs composant
Menu = tkinter.Menu(BarreMenue, tearoff = 0, font= ("Times New Roman", 12))
Menu.add_command(label = "Connexion", command = Connexion,)
Menu.add_command(label = "Deconnexion")
Menu.add_command(label = "Fermer", command = GC.quit)


Categorie = tkinter.Menu(BarreMenue, tearoff = 0, font= ("Times New Roman", 12))
Categorie.add_command(label = "Nouvelle Categorie", command= newCategorie)
Categorie.add_command(label = "Listes des Categorie", command= ListeCategorie)


Produit = tkinter.Menu(BarreMenue, tearoff = 0, font= ("Times New Roman", 12))
Produit.add_command(label = "Nouveau Produit", command= AjouterProduit)
Produit.add_command(label = "Liste des produits", command= ListeProduit)


Client = tkinter.Menu(BarreMenue, tearoff = 0, font= ("Times New Roman", 12))
Client.add_command(label = "Nouveau Client")
Client.add_command(label = "Liste des clients")

Fournisseur = tkinter.Menu(BarreMenue, tearoff = 0, font= ("Times New Roman", 12))
Fournisseur.add_command(label = "Nouveau Fournisseur")
Fournisseur.add_command(label = "Liste des Fournisseurs")

Commande_Fournisseur = tkinter.Menu(BarreMenue, tearoff = 0, font= ("Times New Roman", 12))
Commande_Fournisseur.add_command(label = "Nouvelle commande")
Commande_Fournisseur.add_command(label = "Liste des commandes")

Commande_Client = tkinter.Menu(BarreMenue, tearoff = 0, font= ("Times New Roman", 12))
Commande_Client.add_command(label = "Nouvelle commande")
Commande_Client.add_command(label = "Liste des commandes")

Achats = tkinter.Menu(BarreMenue, tearoff = 0, font= ("Times New Roman", 12))
Achats.add_command(label = "Nouvelle achat")
Achats.add_command(label = "Liste des Achats")

Ventes = tkinter.Menu(BarreMenue, tearoff = 0, font= ("Times New Roman", 12))
Ventes.add_command(label = "Nouvelle Vente")
Ventes.add_command(label = "Liste des ventes")


Dette = tkinter.Menu(BarreMenue, tearoff= 0, font= ("Times New Roman", 12))

#Creation sous menue

Dette_Fournisseur = tkinter.Menu(Dette, tearoff= 0, font= ("Times New Roman", 12))
Dette_Fournisseur.add_command(label="Nouvelle Dette")
Dette_Fournisseur.add_command(label= "Liste des dettes")

Dette_Client = tkinter.Menu(Dette, tearoff= 0, font= ("Times New Roman", 12))
Dette_Client.add_command(label="Nouvelle Dette")
Dette_Client.add_command(label= "Liste des dettes")

#Attachement
Dette.add_cascade(label= "Dettes Fournisseurs", menu= Dette_Fournisseur)
Dette.add_cascade(label="Dettes Clients", menu= Dette_Client)



GestionUtilisateur = tkinter.Menu(BarreMenue, tearoff = 0, font= ("Times New Roman", 12))
GestionUtilisateur.add_command(label = "Nouveau Utilisateur")
GestionUtilisateur.add_command(label = "Liste Utilisateur")

Apropos = tkinter.Menu(BarreMenue, tearoff = 0)


#Creation des cascade(attachement des menu sur la barre du menu)
BarreMenue.add_cascade(label = "Menu", menu = Menu)
BarreMenue.add_cascade(label = "Categorie", menu = Categorie)
BarreMenue.add_cascade(label = "Produits", menu = Produit)
BarreMenue.add_cascade(label = "Clients", menu = Client)
BarreMenue.add_cascade(label = "Fournisseurs", menu = Fournisseur)
BarreMenue.add_cascade(label = "Commandes Fournisseurs", menu = Commande_Fournisseur)
BarreMenue.add_cascade(label = "Commandes Clients", menu = Commande_Client)
BarreMenue.add_cascade(label = "Achats", menu = Achats)
BarreMenue.add_cascade(label = "Ventes", menu = Ventes)
BarreMenue.add_cascade(label = "Dettes", menu = Dette)
BarreMenue.add_cascade(label = "Gestions Utilisateurs", menu = GestionUtilisateur)
BarreMenue.add_cascade(label = "Apropos", menu = Apropos)

#Accrochage du Menu
GC.config(menu = BarreMenue)

#Boucle principale
GC.mainloop()