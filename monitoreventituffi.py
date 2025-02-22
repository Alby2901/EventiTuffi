"""
monitoreventituffi.py

Questo script Python recupera gli eventi di tuffi dal sito web della Federazione Italiana Nuoto,
li confronta con gli eventi precedenti e invia email di notifica per eventuali nuovi eventi o modifiche.
"""
import logging
import web_scraper
import data_extractor
import utility
import mail_sender
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)  # Ottieni un logger con il nome del modulo

# logger.info("Programma avviato.")  # Messaggio informativo
# logger.debug(f"Variabile eventi: {eventi}")  # Messaggio di debug
# logger.error(f"Errore durante la richiesta: {e}")  # Messaggio di errore

def main():
    """
    Funzione principale del programma.
    Recupera gli eventi dal sito web, li confronta con gli eventi precedenti e invia email di notifica.

    Args:
        Nessun argomento.

    Returns:
        Nessun valore restituito.
    """

    logger.info("Programma avviato.")  # Messaggio informativo
    # esegue il parsing della pagina eventi
    soup = web_scraper.recupera_e_parsa_pagina('https://www.federnuoto.it/home/tuffi/eventi-tuffi.html')
    # crea un array di oggetti evento con i dati estratti
    eventi = data_extractor.estrai_eventi(soup)
    
    if eventi:
        # per ogni evento esegue il parsing della pagina dell'evento e inserisce nell'oggetto la proprità
        # dettagli_evento con i dati estratti
        i = 1
        for evento in eventi:
            # Estrazione dati dalla pagina dei dettagli dell'evento
            logger.debug(f"Inizio estrazione dettagli evento n. {str(i)}")
            soup_evento = web_scraper.recupera_e_parsa_pagina('https://www.federnuoto.it' + evento.get('url'))
            logger.debug(f"Fine estrazione dettagli evento n. {str(i)}")
            
            # Elaborazione dati della pagina dei dettagli dell'evento
            logger.debug(f"Inizio elabor. dettagli evento n. {str(i)}")
            dettagli_evento = data_extractor.estrai_dettagli_evento(soup_evento)
            logger.debug(f"Variabile dettagli_evento: {dettagli_evento}")
            logger.debug(f"Fine elabor. dettagli evento n. {str(i)}")

            # Aggiunta dei dettagli dell'evento all'oggetto evento
            evento["eve-details"] = dettagli_evento
            
            i += 1
            time.sleep(1)
            logger.debug(f"Variabile evento: {evento}")

    # Carica gli eventi precedenti
    eventi_precedenti = utility.carica_eventi("eventi.json")

    logger.debug(f"Variabile eventi_precedenti: {eventi_precedenti}")

    # Confronta gli eventi attuali con quelli precedenti
    nuovi_eventi, eventi_modificati = utility.confronta_eventi(eventi, eventi_precedenti)  # Gestisci le due liste      
    logger.debug(f"Variabile nuovi_eventi: {str(nuovi_eventi)}")
    logger.debug(f"Variabile eventi_modificati: {str(eventi_modificati)}")


    # Invia email di notifica se ci sono nuovi eventi o eventi modificati
    if nuovi_eventi or eventi_modificati:
        mail_sender.invia_email_notifiche(nuovi_eventi, eventi_modificati)
        utility.salva_eventi(eventi, "eventi.json")

    logger.info("Programma terminato.")  # Messaggio informativo


# Funzione di test per l'invio di email
def test_mail_send():
    mail_sender.invia_email_test()


if __name__ == "__main__":
    main()
    # test_mail_send()
