import smtplib
from email.mime.text import MIMEText

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Accesso alle variabili
mittente = config['ImpostazioniEmail']['mittente']
password = config['ImpostazioniEmail']['password']
server_smtp = config['ImpostazioniEmail']['server_smtp']
porta_smtp = int(config['ImpostazioniEmail']['porta_smtp'])  # Conversione a intero
oggetto_email = config['ImpostazioniEmail']['oggetto_email']

lista_destinatari_str = config['Destinatari']['lista_destinatari']
lista_destinatari = [email.strip() for email in lista_destinatari_str.split(',')]



def invia_email_notifiche(nuovi_eventi, eventi_modificati):
    # Configurazione dell'email
    mittente = "mammamituffo@gmail.com"  # Sostituisci con la tua email
    destinatario = "a.azzola@scriptanet.it"  # Sostituisci con l'email del destinatario
    password = "qdlargsjhdlwjpiv"  # Sostituisci con la tua password
    server_smtp = "smtp.gmail.com"  # Server SMTP di Gmail
    porta_smtp = 587  # Porta SMTP di Gmail (utilizza la porta 465 per SSL)

    # Funzione per creare il corpo dell'email
    def crea_corpo_email(eventi, tipo_evento):
        corpo = f"Sono stati trovati i seguenti {tipo_evento}:\n\n"
        for evento in eventi:
            corpo += f"- Titolo: {evento['titolo']}\n"
            corpo += f"- Data inizio: {evento['data_inizio_gg']}/{evento['data_inizio_mm']}/{evento['data_inizio_yy']}\n"
            corpo += f"- Data fine: {evento['data_fine_gg']}/{evento['data_fine_mm']}/{evento['data_fine_yy']}\n"
            corpo += f"- Luogo: {evento['luogo']}\n"
            corpo += f"- URL: {evento['url']}\n"
            if evento.get('eve-details'):  # Verifica se 'eve-details' è presente
                corpo += f"- Dettagli: {evento['eve-details']}\n"
            corpo += "\n"
        return corpo

    try:
        # Connessione al server SMTP
        server = smtplib.SMTP(server_smtp, porta_smtp)
        server.starttls()  # Avvia la connessione TLS (obbligatoria per Gmail)
        server.login(mittente, password)

        # Invio email nuovi eventi
        if nuovi_eventi:
            corpo_nuovi_eventi = crea_corpo_email(nuovi_eventi, "nuovi eventi")
            messaggio_nuovi_eventi = MIMEText(corpo_nuovi_eventi)
            messaggio_nuovi_eventi["Subject"] = "Nuovi eventi di tuffi"
            messaggio_nuovi_eventi["From"] = mittente
            messaggio_nuovi_eventi["To"] = destinatario
            server.sendmail(mittente, destinatario, messaggio_nuovi_eventi.as_string())

        # Invio email eventi modificati
        if eventi_modificati:
            corpo_eventi_modificati = crea_corpo_email(eventi_modificati, "eventi modificati")
            messaggio_eventi_modificati = MIMEText(corpo_eventi_modificati)
            messaggio_eventi_modificati["Subject"] = "Eventi di tuffi modificati"
            messaggio_eventi_modificati["From"] = mittente
            messaggio_eventi_modificati["To"] = destinatario
            server.sendmail(mittente, destinatario, messaggio_eventi_modificati.as_string())

        print("Email inviate con successo!")

    except Exception as e:
        print(f"Errore durante l'invio dell'email: {e}")

    finally:
        server.quit()  # Chiude la connessione al server SMTP

def invia_email_test():

    # Configurazione dell'email
    # mittente = "mammamituffo@gmail.com"  # Sostituisci con la tua email
    # destinatario = "a.azzola@scriptanet.it"  # Sostituisci con l'email del destinatario
    # password = "qdlargsjhdlwjpiv"  # Sostituisci con la tua password
    # server_smtp = "smtp.gmail.com"  # Server SMTP di Gmail
    # porta_smtp = 587  # Porta SMTP di Gmail (utilizza la porta 465 per SSL)

    try:
        # Connessione al server SMTP
        # print(f"mittente: {mittente}")
        # print(f"password: {password}")
        # print(f"server_smtp: {server_smtp}")
        # print(f"porta_smtp: {porta_smtp}")
        # print(f"lista_destinatari: {lista_destinatari}")
        
        
        server = smtplib.SMTP(server_smtp, porta_smtp)
        server.starttls()  # Avvia la connessione TLS (obbligatoria per Gmail)
        server.login(mittente, password)

        corpo_nuovi_eventi = "corpo della mail"
        messaggio_nuovi_eventi = MIMEText(corpo_nuovi_eventi)
        messaggio_nuovi_eventi["Subject"] = "Nuovi eventi di tuffi"
        messaggio_nuovi_eventi["From"] = mittente
        # messaggio_nuovi_eventi["To"] = destinatario
        messaggio_nuovi_eventi["To"] = ", ".join(lista_destinatari) 
        server.sendmail(mittente, lista_destinatari, messaggio_nuovi_eventi.as_string())

        print("Email inviate con successo!")

    except Exception as e:
        print(f"Errore durante l'invio dell'email: {e}")

    finally:
        server.quit()  # Chiude la connessione al server SMTP
