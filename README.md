Questo progetto ha lo scopo di creare un parser di una pagina webche, girando gionalmente, verifica se ci sono stati cambiamenti e in caso positivo, invia una notififa via mail.

In partocolare, lo scopo di questo sistema, è di leggere una pagina che contiene informazioni su eventi in calendario e di notificare se sono stati aggiunti o modificati eventi rispetto al controllo precedente. 
La pagina che viene letta è questa: https://www.federnuoto.it/home/tuffi/eventi-tuffi.html e per ciascun evento viene letta anche la pagina cillegata che contien maggiori dettagli e che possono variare nel tempo.

Più in dettaglio si tratta di un progetto scrippo in Pyton.
I passi principali del sistema sono:
 - lettura della pagina degli eventi (librerie requests e BeautifulSoup)
 - decodifica della parte specifica relativa agli eventi
 - se ci sono eventi, lettura della pagina collegata ad ogni evento
 - creazione di una lista di oggettti di tipo "evento" con le informazioni raccolte
 - comparazione della lista degli oggetti appena creata con la lista analoga salvata durante la precedente esecuzione del sistema
 - se vengono rilevate differenze creazione e invio di notifica via mail:
   - una per segnalare nuovi eventi e una per segnalare modifiche ad un evento 

Il sistema deve essere installato su un computer (server o client) che possa eseguire il comando temporizzato secondo le necessita: in questo caso una esecuzione giornaliera
Essendo un progetto Pyton richiede che Pyton sia installato sul computer che esegue il programma.

Il progetto Pyton è stato creato in un enviroment.

Per essere eseguito correttament il progetto richiede un file denominato "config.ini" che deve contenere le seguenti informazioni:

      [ImpostazioniEmail]
      mittente = mammamituffo@gmail.com
      password = 1234567890
      server_smtp = smtp.gmail.com
      porta_smtp = 587
      oggetto_email = Nuovi eventi di tuffi
      
      [Destinatari]
      lista_destinatari = a.azzola@scriptanet.it, mammamituffo@gmail.com, alberto.azzola@gmail.com

I dati devono essere modificati secondo il proprio ambiente:

