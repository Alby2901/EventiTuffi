import requests
from bs4 import BeautifulSoup

def recupera_e_parsa_pagina(url):
    # ... (codice per recuperare la pagina e gestire le richieste, come prima)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6,mt;q=0.5,es;q=0.4,fr;q=0.3",
        "Cache-Control": "max-age=0",
        "Cookie": "CookieConsent={stamp:'IupX8H2MQByHJ6OkV6tV5h07Jfa3CdZW37eiTq4xeq152kyW7v/zTQ==',necessary:true,preferences:false,statistics:false,marketing:false,method:'explicit',ver:1,utc:1729950414219,region:'it'}; 2dbed83899cc2b64df591c1893e41fbe=6f3a0ed1ad1b893b16ee2233367149ce; GCLB=CP_-wMvBx8jC6QEQAw; _pk_id.100.f6e8=37c0c22101fabccf.1738769996.; _pk_ses.100.f6e8=1; _iub_cs-50053366=%7B%22timestamp%22%3A%222025-02-05T15%3A40%3A00.391Z%22%2C%22version%22%3A%221.75.1%22%2C%22purposes%22%3A%7B%221%22%3Atrue%2C%223%22%3Atrue%2C%224%22%3Atrue%7D%2C%22id%22%3A50053366%2C%22cons%22%3A%7B%22rand%22%3A%22157518%22%7D%7D; _iub_previous_preference_id=2025/02/05/15/40/00/391/157518",
        "Referer": url,
        "Sec-CH-UA": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1"
    }

    try:
        # print("Recupero la pagina => " + url)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la richiesta: {e}")
        return None
