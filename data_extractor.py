def estrai_eventi(soup):
    print('Inizio estrai_eventi...')
    eventi = []
    
    # ... (codice per estrarre i dati dagli eventi dal codice HTML parsato, come prima)
    # Trova il contenitore principale degli eventi
    eventi_container = soup.find("div", class_="eve_list")

    if eventi_container:
        # Trova tutti i singoli eventi
        eventi_items = eventi_container.find_all("div", class_="eve_container")

        for evento_item in eventi_items:
            evento = {}

            # Estrai URL
            link = evento_item.find("a", class_="eve")
            if link:
                evento["url"] = link["href"]

            # Estrai date
            date_spans = evento_item.find_all("span", class_="eve_date_d")
            if len(date_spans) >= 2:
                data_inizio_gg = date_spans[0].text.strip()
                data_fine_gg = date_spans[1].text.strip()
                
            date_spans = evento_item.find_all("span", class_="eve_date_m")
            if len(date_spans) >= 2:
                data_inizio_mm = date_spans[0].text.strip()
                data_fine_mm = date_spans[1].text.strip()
                
            date_spans = evento_item.find_all("span", class_="eve_date_y")
            if len(date_spans) >= 2:
                data_inizio_yy = date_spans[0].text.strip()
                data_fine_yy = date_spans[1].text.strip()

            evento["data_inizio_gg"] = data_inizio_gg
            evento["data_inizio_mm"] = data_inizio_mm
            evento["data_inizio_yy"] = data_inizio_yy
                                        
            evento["data_fine_gg"] = data_fine_gg
            evento["data_fine_mm"] = data_fine_mm
            evento["data_fine_yy"] = data_fine_yy

            # Estrai titolo
            title_span = evento_item.find("span", class_="eve_title").find("span")
            if title_span:
                evento["titolo"] = title_span.text.strip()

            # Estrai luogo
            luogo_span = evento_item.find("span", class_="eve_loc")
            if luogo_span:
                evento["luogo"] = luogo_span.text.strip()

            eventi.append(evento)
    
    return eventi

def estrai_dettagli_evento(soup):
    print('====>>>>>')
    # print(soup)
    dettagli_div = soup.find("div", class_="eve_details")
    if dettagli_div:
        return str(dettagli_div)  # Restituisci il contenuto come stringa
    else:
        return None  # Restituisci None se il div non viene trovato
    