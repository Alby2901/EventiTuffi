import web_scraper
import data_extractor
import utility
import mail_sender
import time

def main():
    """
    Funzione principale del programma.
    Recupera gli eventi dal sito web, li confronta con gli eventi precedenti e invia email di notifica.

    Args:
        Nessun argomento.

    Returns:
        Nessun valore restituito.
    """

    # esegue il parsing della pagina eventi
    soup = web_scraper.recupera_e_parsa_pagina('https://www.federnuoto.it/home/tuffi/eventi-tuffi.html')
    # crea un array di oggetti evento con i dati estratti
    eventi = data_extractor.estrai_eventi(soup)
    
    if eventi:
        # per ogni evento esegue il parsing della pagina dell'evento e inserisce nell'oggetto la proprità
        # dettagli_evento con i dati estratti
        i = 1
        for evento in eventi:
            soup_evento = web_scraper.recupera_e_parsa_pagina('https://www.federnuoto.it' + evento.get('url'))
            print('Estrazioe Evento n. ' + str(i))
            dettagli_evento = data_extractor.estrai_dettagli_evento(soup_evento)
            # print(dettagli_evento)
            print('Estrazioe Dettagli Evento n. '  + str(i))
            evento["eve-details"] = dettagli_evento
            print('Estratti Evento e Dettahli Evento n. '  + str(i))
            i += 1
            time.sleep(1)
            # print(evento)

    eventi_precedenti = utility.carica_eventi("eventi.json")

    # print(eventi_precedenti)

    nuovi_eventi, eventi_modificati = utility.confronta_eventi(eventi, eventi_precedenti)  # Gestisci le due liste
    print('Nuovi eventi => ' + str(nuovi_eventi))    
    print('Eventi modificati => ' + str(eventi_modificati))

    if nuovi_eventi or eventi_modificati:
        mail_sender.invia_email_notifiche(nuovi_eventi, eventi_modificati)
        utility.salva_eventi(eventi, "eventi.json")

    # Stampa temporanea per controllo dati ricevuti
    # if eventi:
    #     for evento in eventi:
    #         print(evento)
def test_mail_send():
    mail_sender.invia_email_test()

if __name__ == "__main__":
    main()
    # test_mail_send()
