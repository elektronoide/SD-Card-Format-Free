# Software Name: SD-Card Format Free
# Author: Bocaletto Luca
import tkinter as tk
from tkinter import ttk
import subprocess
import ctypes
import psutil

# Funzione per ottenere una lista delle unità rimovibili
def get_removable_drives():
    drives = []
    for drive in psutil.disk_partitions():
        if "removable" in drive.opts:
            drives.append(drive.device)
    return drives

# Funzione per formattare la scheda di memoria SD
def formatta_scheda():
    dispositivo = dispositivo_combobox.get()
    try:
        comando = f"format {dispositivo} /FS:FAT32"
        subprocess.run(comando, shell=True, check=True)
        messagebox.showinfo("Formattazione Completata", f"La scheda {dispositivo} è stata formattata con successo.")
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, f"Impossibile formattare la scheda {dispositivo}.\nErrore: {str(e)}", "Errore", 0)

# Funzione per aggiornare la lista delle unità rimovibili
def refresh_drives():
    dispositivi = get_removable_drives()
    dispositivo_combobox['values'] = dispositivi

# Creazione della finestra principale
root = tk.Tk()
root.title("Applicativo per Formattare Schede di Memoria SD")

# Etichetta e combobox per selezionare l'unità
dispositivo_label_title = tk.Label(root, text="SD-Card Format Free")
dispositivo_label = tk.Label(root, text="Seleziona un'Unità Rimovibile:")
dispositivo_label_title.pack()
dispositivo_label.pack()
dispositivo_combobox = ttk.Combobox(root, state="readonly")
dispositivo_combobox.pack()

# Pulsante per aggiornare la lista delle unità rimovibili
aggiorna_button = tk.Button(root, text="Aggiorna", command=refresh_drives)
aggiorna_button.pack()

# Pulsante per avviare la formattazione
formatta_button = tk.Button(root, text="Formatta", command=formatta_scheda)
formatta_button.pack()

# Esegui l'aggiornamento iniziale della lista delle unità rimovibili
refresh_drives()

# Esecuzione del loop principale della GUI
root.mainloop()
