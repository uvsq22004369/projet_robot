##################################################
# Projet Robot Ricochet
# Groupe BI: 1
# Mathieu LAM
# Océane MACHADO
# Aurélie ALVET
# Timothé PEYREIGNE
# Thushanth JEYAKANTHN
# Yanis MERBAH
# https://github.com/uvsq21915611/projet_robot
###################################################

import tkinter as tk
racine = tk.Tk()
racine.title("Projet robot ricochet")
racine.configure(width = 300, height = 300, bg ='beige')

c = 50                         # Longueur d'un côté d'une case
n = 16                         # Nombre de cases par ligne et par colonne
cases = []
WIDTH = n*c+2
HEIGHT = WIDTH
couleur = ""
# position initiale des robots :
X1 = 177
Y1 = 577
X2 = 427
Y2 = 477
X3 = 477
Y3 = 327
X4 = 75
Y4 = 625
#

def grille():
    for ligne in range(n):
        transit = []
        for colonne in range(n):
            transit.append(canvas.create_rectangle(colonne*c+2, ligne*c+2, (colonne+1)*c+2, (ligne+1)*c+2))
        cases.append(transit)

#Crée les robot et leurs paramètres
def robot_rouge():
    couleur = "rouge"
    dx, dy = 1, 2
    rayon = 20
    cercle = canvas.create_oval((X2-rayon, Y2-rayon),
                                (X2+rayon, Y2+rayon),
                                fill="red")
    return [cercle, dx, dy]

def robot_jaune():
    couleur = "jaune"
    dx, dy = 1, 2
    rayon = 20
    cercle = canvas.create_oval((X4-rayon, Y4-rayon),
                                (X4+rayon, Y4+rayon),
                                fill="yellow")
    return [cercle, dx, dy]

def robot_vert():
    couleur = "vert"
    dx, dy = 1, 2
    rayon = 20
    cercle = canvas.create_oval((X1-rayon, Y1-rayon),
                                (X1+rayon, Y1+rayon),
                                fill="green")
    return [cercle, dx, dy]

def robot_bleu():
    couleur = "bleu"
    dx, dy = 1, 2
    rayon = 20
    cercle = canvas.create_oval((X3-rayon, Y3-rayon),
                                (X3+rayon, Y3+rayon),
                                fill="blue")

    return [cercle, dx, dy]

#Définit quel robot de couleur est actuellement sélectionné
def selectionne():
    pass

#Associe les touches directionnelles du clavier "haut","bas","gauche","droite" au déplacement du robot
def Clavier():
    pass

#Permet de faire arrêter le robot s'il rencontre un obstacle / distance maximale de déplacement autorisé
def bounce():
    pass

#Affiche un rectangle de couleur permettant de montrer les directions possibles par le robot 
def show_Path():
    pass

#Fait recommencer le jeu
def reset():
    pass

#Affiche le score / liste des meilleurs scores
def score():
    pass

#Affiche le nombre de mouvements effectués
def compteur():
    pass

#Permet d'enregistrer l'état de la partie (position des robots/nombres de mouvements/ ect ... )
def save():
    pass

#Permet de charger les éléments précédemment sauvegardés
def load():
    pass

#Permet d'éditer le plateau en rajoutant des éléments 
def editor():
    pass

#Permet d'afficher les dernier mouvement fait
def move(event):
    pass



canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="white")
canvas.grid(row=1, column=0)
canvas.bind('<Key>', Clavier)

canvas_move = tk.Canvas(racine, width= WIDTH/5, height= HEIGHT, bg="black")
canvas_move.bind('Key', move)
canvas_move.grid(row=1, column=1)

carre_restart = canvas.create_rectangle(350+2, 350+2, 450+2, 450+2, fill="black")

sauvegarde = tk.Button(racine, text="sauvegarder", command=save())
sauvegarde.grid(row=1, column= 3)

racine.mainloop()
