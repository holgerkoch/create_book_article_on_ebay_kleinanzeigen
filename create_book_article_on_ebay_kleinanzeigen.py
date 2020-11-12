# Programm, um sehr schnell und einfach Bücher Anzeigen auf ebay-kleinanzeigen zu erstellen.
# Die Idee dahinter: Bücher zu versenden lohnt sich nicht, wegwerfen will man sie aber auch nicht. 
# Vielleicht hat aber jemand aus der Nachbarschaft daran Interesse?
# Sprich es muss sehr einfach sein und schnell gehen, die Bücher bei ebay-kleinanzeigen.de einzustellen.
# Einfach die ISBN Nummer eingeben oder mittels Barcode Scanner einscannen, der Rest geschieht automatisiert.
# Dazu wird eine config.json Datei mit den Anzeigen generiert. Anschließend kann diese mit
# https://github.com/donwayo/ebayKleinanzeigen
# eingelesen und die Anzeigen veröffentlicht werden.

# 1. lesen des ISBN Barcodes per Scanner oder von Hand eingeben
# 2. beschaffen der Informationen per Google ISBN Suche
# 3. Generierung der Anzeige und hinzufügen zur config.json
# 4. Nachdem das letzte Buch eingescannt wurde, einfach Enter drücken und kleinanzeigen.py wird angestartet.
# 5. kleinanzeigen.py liest die Anzeigen ein und erstellt diese mittels gecko und selenium.

# Konfiguration:
# bookPrice definiert den Verkaufspreise, default 1€
# letzte Zeile zum Aufruf von kleinanzeigen.py anpassen (ACHTUNG: kleinanzeigen.py muss fertig konfiguriert und eingerichtet sein, 
# siehe Anleitung: https://github.com/donwayo/ebayKleinanzeigen/blob/master/README.md )
# os.system("C:\\Users\\ulrik\\AppData\\Local\\Programs\\Python\\Python39\\python.exe kleinanzeigen.py --profile config.json")

import requests
import json
import os

# Define some parameters
bookPrice = "1"

def profile_read(profile, config):
    if os.path.isfile(profile):
        with open(profile, encoding="utf-8") as file:
            config.update(json.load(file))


def profile_write(profile, config):
    with open(profile, "w+", encoding='utf8') as fh_config:
        text = json.dumps(config, sort_keys=True, indent=4, ensure_ascii=False)
        fh_config.write(text)

sProfile = "config.json"
# Variable zum speichern der Configdatei
config = {}

# Einlesen der kompletten Config Datei
profile_read(sProfile, config)

while True:
    # Eingabe der ISBN Nummer, entweder von Hand oder per Barcodescanner
    isbnNumber = input("Enter a isbn number: ")

    if isbnNumber == "":
        break
    else:
        print("ISBN Nummer: ", isbnNumber) 

    # beschaffen der Buchinformationen per Google API
    # https://www.googleapis.com/books/v1/volumes?q=isbn:0771595158
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(isbnNumber))

    # print("Returncode: ", r.status_code)
    # print("Headers: ", r.headers)
    # print("Inhalt: ", r.text)

    # Antwort als json laden
    bookInformation = json.loads(r.text)

    # Infos parsen
    bookTitle = bookInformation['items'][0]['volumeInfo']['title']
    bookSubtitle = bookInformation['items'][0]['volumeInfo']['subtitle']
    bookAuthor = bookInformation['items'][0]['volumeInfo']['authors']
    bookAnzahlSeiten = bookInformation['items'][0]['volumeInfo']['pageCount']
    bookImageURL = bookInformation['items'][0]['volumeInfo']['imageLinks']['thumbnail']

    print("bookTitle", bookTitle)
    print("bookSubtile", bookSubtitle)
    print("bookAuthor", bookAuthor)
    print("bookAnzahlSeiten", bookAnzahlSeiten)
    print("bookImageURL", bookImageURL)

    # download the book image from google
    open(str(isbnNumber) + ".jpg", 'wb').write(requests.get(bookImageURL, allow_redirects=True).content)

    temp = config['ads'] 
    print("temp: ", temp)

    # python object to be appended 
    y = { "title": "Gut erhaltenes Buch: " + bookTitle,
        "desc": "Angeboten wird das Buch " + bookTitle + ", " + bookSubtitle + " von " + bookAuthor[0] + " mit insgesamt " + str(bookAnzahlSeiten) + " Seiten.",
        "enabled": "1",
        "price": bookPrice,
        "price_type": "NEGOTIABLE",
        "caturl": "https://www.ebay-kleinanzeigen.de/p-kategorie-aendern.html#?path=73/76/unterhaltungsliteratur&isParent=false",
        "shipping_type": "PICKUP",
        "photofiles": [ str(isbnNumber) + ".jpg" ],
        "zip" : "99099"
      }
  
  
    # appending data to emp_details  
    temp.append(y) 

profile_write(sProfile, config)

# Aufruf von kleinanzeigen.py, um die neuen Anzeigen hochzuladen
os.system("C:\\Users\\ulrik\\AppData\\Local\\Programs\\Python\\Python39\\python.exe kleinanzeigen.py --profile config.json")