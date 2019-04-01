# coding: utf-8
from tkinter import *
#importe les alertes
from tkinter import ttk
from tkinter.messagebox import *


def inicialisation():
    global chaine
    chaine = entree.get()
    chaine = chaine.lower()
    liste = [elt for elt in chaine]
    nombre_de_lettres = len(liste)

    global dico_ponctuation
    dico_ponctuation = {",": ",", "?": "?", ".": ".", ";": ";", "!": "!", "'": "'", "&": "1", "é": "2", "#": "3", "{": "4",
                        "[": "5", "|": "6", "è": "7", "_": "8", "ç": "9", "(": "(", ")": ")"}

    global key
    key = entreen.get()
    key = int(key)
    if key>25:
        key = 25
    liste_code = ["z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                  "t",
                  "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                  "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "z", "a", "b", "c", "d", "e", "f", "g",
                  "h",
                  "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                  "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
                                                                         "z", "a", "b", "c", "d", "e", "f", "g", "h",
                  "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                  "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "z", "a", "b", "c", "d", "e", "f", "g",
                  "h",
                  "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                  "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a"
                  ]
    liste_code.reverse()
    resultat = []
    if nombre_de_lettres<0:
        print ("le nombre de lettre egale {}".format(nombre_de_lettres))
        error_nombre_de_lettres(nombre_de_lettres)
    else:
        compteur_de_transformation(nombre_de_lettres, liste, liste_code, key, resultat)



def compteur_de_transformation(nombre,liste, liste_code, key, resultat):
    i = 0
    h = 0
    while h != (nombre):
        h = h+1
        i = i+1
        if i == 27:
            i = 1


        transformateur_de_lettre(i, liste_code, liste, key, resultat)
    label = Label(fenetre, text="".join(resultat))
    label.pack()


def transformateur_de_lettre(i, liste_code, liste, key, resultat):
    lettre = (liste[i-1])
    if lettre.lower() == "a":
        n = key + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "b":
        n = key + 1 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "c":
        n = key + 2 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "d":
        n = key + 3 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "e":
        n = key + 4 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "f":
        n = key + 5 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "g":
        n = key + 6 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "h":
        n = key + 7 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "i":
        n = key + 8 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "j":
        n = key + 9 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "k":
        n = key + 10 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "l":
        n = key + 11 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "m":
        n = key + 12 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "n":
        n = key + 13 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "o":
        n = key + 14 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "p":
        n = key + 15 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "q":
        n = key + 16 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "r":
        n = key + 17 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "s":
        n = key + 18 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "t":
        n = key + 19 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "u":
        n = key + 20 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "v":
        n = key + 21 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "w":
        n = key + 22 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "x":
        n = key + 23 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "y":
        n = key + 24 + i
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == "z":
        n = key + i - 1
        lettre_code = (liste_code[n])
        resultat.append(lettre_code)
    elif lettre.lower() == " ":
        lettre_code = " "
        resultat.append(lettre_code)
    elif lettre.lower() in dico_ponctuation.values():
        resultat.append(dico_ponctuation[lettre.lower()])
    else:
        resultat.append(" error ")

def error_nombre_de_lettres(nombre_de_lettres):
    showwarning('Error', ("le nombre de lettre est supérieur à 120 ({})".format(nombre_de_lettres)))
    pass

def recupere_mot():
    showinfo("information", ("Vous n'êtes pas obliger de valider.  mot = {}".format(entree.get())))
    global chaine
    chaine = entree.get()


def recupere_nombre():
    showinfo("information", ("Vous n'êtes pas obliger de valider.  Clé = {}".format(entreen.get())))
    global key
    key = entreen.get()



def codage():
     inicialisation()
     pass

fenetre = Tk()
fenetre. title('Code César')
fenetre.iconbitmap("image_infini.ico")
fenetre.resizable(False, False)

label = Label(fenetre, text="Ceci est un décodeur César. Tapez votre mot dans la case 'mot' ( MAX: 120 lettres )."
                            " La clé est à remplir dans la case 2 (max 25)")
label.pack()

value = StringVar()
value.set("5")
entree = ttk.Entry(fenetre, textvariable=value, width=30)
entree.pack()


#bouton valider mot
bouton = ttk.Button(fenetre, text="Valider le mot", command=recupere_mot)
bouton.pack()

value = StringVar()
value.set("2")
entreen = ttk.Entry(fenetre, textvariable=value, width=30)
entreen.pack()

bouton = ttk.Button(fenetre, text="valider la cle", command=recupere_nombre)
bouton.pack()



bouton = ttk.Button(fenetre, text="commencer le codage", command=codage).pack(side=TOP, padx=5, pady=5)


fenetre.mainloop()

exit()



