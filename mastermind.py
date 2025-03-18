import tkinter as tk
import random

couleurs = ["red", "green", "blue", "cyan", "yellow", "white", "pink", "purple"]
tentatives_max = 10

CANVAS_WIDTH, CANVAS_HEIGHT= 900, 700
root = tk.Tk()
root.title("Mastermind")
canvas_accueil = tk.Canvas(root, width= CANVAS_WIDTH, height= CANVAS_HEIGHT, background= "LightBlue1")
canvas_accueil.grid()
label = tk.Label(root, text= "Jouons au Mastermind!", font= ("helvetica", "30"),)
label.place(x= 250, y= 10)

def solo(): #définie le mode de jeu à 1 joueur
    code_solo = random.sample(couleurs, 4)
    print(code_solo)
    canvas_solo = tk.Toplevel(root, width= CANVAS_WIDTH, height= CANVAS_HEIGHT, background= "LightBlue1")
    canvas_solo.transient(root)

def multi(): #définie le mode de jeu à 2 joueurs
    canvas_multi = tk.Toplevel(root, width= CANVAS_WIDTH, height= CANVAS_HEIGHT, background= "LightBlue1")
    canvas_multi.transient(root)

bouton_solo = tk.Button(root, text= "1 joueur", font= ("helvetica", "20"),
                        activebackground= "#BCBCBC", command= solo)
bouton_solo.place(x= 390, y= 200)

bouton_multi = tk.Button(root, text= "2 joueurs", font= ("helvetica", "20"),
                         activebackground= "#BCBCBC", command= multi)
bouton_multi.place(x= 388, y= 300)



root.mainloop()

