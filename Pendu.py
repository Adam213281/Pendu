import random
import tkinter as tk
from tkinter import messagebox

mots = ["python", "ordinateur", "programmation", "interface", "souris", "clavier"]
mot_a_trouver = random.choice(mots)
lettres_trouvees = ["_" for _ in mot_a_trouver]
nb_essais = 6

def verifier_lettre():
    global nb_essais
    lettre = entry_lettre.get().lower()
    entry_lettre.delete(0, tk.END)
    
    if lettre in mot_a_trouver:
        for i, l in enumerate(mot_a_trouver):
            if l == lettre:
                lettres_trouvees[i] = lettre
    else:
        nb_essais -= 1
    
    label_mot.config(text=" ".join(lettres_trouvees))
    label_essais.config(text=f"Essais restants : {nb_essais}")
    
    if "_" not in lettres_trouvees:
        messagebox.showinfo("Félicitations!", "Vous avez gagné!")
        root.quit()
    elif nb_essais == 0:
        messagebox.showerror("Perdu...", f"Le mot était : {mot_a_trouver}")
        root.quit()

root = tk.Tk()
root.title("Jeu du Pendu")

label_mot = tk.Label(root, text=" ".join(lettres_trouvees), font=("Arial", 20))
label_mot.pack()

label_essais = tk.Label(root, text=f"Essais restants : {nb_essais}", font=("Arial", 14))
label_essais.pack()

entry_lettre = tk.Entry(root)
entry_lettre.pack()

bouton_valider = tk.Button(root, text="Essayer", command=verifier_lettre)
bouton_valider.pack()

root.mainloop()
