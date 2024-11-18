import os
import subprocess
import tkinter as tk
from tkinter import messagebox
import sys

# Chemins dynamiques vers les scripts PowerShell


if getattr(sys, 'frozen', False):
    # Pour l'exécutable .exe
    toggle_script_path = os.path.join(sys._MEIPASS, "toggle_touchscreen.ps1")
    check_status_script_path = os.path.join(sys._MEIPASS, "check_touchscreen_status.ps1")
else:
    # Pour le script Python normal
    toggle_script_path = os.path.join(os.path.dirname(__file__), "toggle_touchscreen.ps1")
    check_status_script_path = os.path.join(os.path.dirname(__file__), "check_touchscreen_status.ps1")

def check_touchscreen_status():
    # Exécuter le script PowerShell pour vérifier l'état de l'écran tactile sans Start-Process
    result = subprocess.run(
        ["powershell", "-ExecutionPolicy", "Bypass", "-File", check_status_script_path],
        capture_output=True, text=True
    )
    output = result.stdout.strip()
    return output == "True"

def toggle_touchscreen():
    try:
        # Exécuter le script PowerShell en mode administrateur pour activer/désactiver l'écran tactile

        result = subprocess.run(
            ["powershell", "-Command", f"Start-Process powershell -ArgumentList '-ExecutionPolicy Bypass -File \"{toggle_script_path}\"' -Verb RunAs"],
            capture_output=True, text=True, shell=True
        )
                # Vérifier l'état après le basculement et afficher le résultat


        # Mettre à jour le texte du bouton après avoir exécuté le script

        # check_touchscreen_status()
        update_button_text()
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'exécution du script PowerShell : {e}")

def update_button_text():
    # Mettre à jour le texte et la couleur du bouton en fonction de l'état de l'écran tactile
    check_touchscreen_status()

    if check_touchscreen_status():
        button_text.set("Désactiver l'écran tactile")
        toggle_button.config(bg="green", activebackground="darkgreen")
    else:
        button_text.set("Activer l'écran tactile")
        toggle_button.config(bg="red", activebackground="darkred")

# Créer l'interface graphique
app = tk.Tk()
app.title("Gestion de l'écran tactile")
app.geometry("300x200")

button_text = tk.StringVar()
button_text.set("Vérification...")  # Texte initial pendant la vérification

# Créer le bouton circulaire
toggle_button = tk.Button(
    app, textvariable=button_text, command=toggle_touchscreen, font=("Arial", 12), 
    width=10, height=2, relief="solid", borderwidth=2
)
toggle_button.pack(pady=50)

# Style pour le bouton : couleur et bordures
toggle_button.config(
    width=20, height=10,  # Taille du bouton (carrée pour être circulaire)
    font=("Arial", 12), 
)

# Vérifie le statut actuel de l'écran tactile et met à jour le texte et la couleur du bouton


update_button_text()

app.mainloop()