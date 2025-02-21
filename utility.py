import json
import smtplib
from email.mime.text import MIMEText

def carica_eventi(nome_file):
    try:
        with open(nome_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Restituisce una lista vuota se il file non esiste


def confronta_eventi(eventi, eventi_precedenti):
    nuovi_eventi = []
    eventi_modificati = []  # Nuova lista per gli eventi modificati
    for evento in eventi:
        evento_presente = False
        for evento_prec in eventi_precedenti:
            if evento["url"] == evento_prec["url"]:  # Confronta per URL
                evento_presente = True
                if evento != evento_prec:  # Confronta tutti i dettagli
                    eventi_modificati.append(evento)  # Aggiungi agli eventi modificati
                break
        if not evento_presente:
            nuovi_eventi.append(evento)
    return nuovi_eventi, eventi_modificati  # Restituisci entrambe le liste


def salva_eventi(eventi, nome_file):
    try:
        with open(nome_file, "w") as f:
            json.dump(eventi, f, indent=4)
    except Exception as e:
        print(f"Errore durante il salvataggio degli eventi: {e}")
