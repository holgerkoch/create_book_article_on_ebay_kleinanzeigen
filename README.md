# create_book_article_on_ebay_kleinanzeigen
Easy and fast way to create an ad for selling books on ebay-kleinanzeigen.de 

We have a lot of books and didn't know what to do with them. Then my wife said that if it weren't so time-consuming, we could post an ad on ebay-kleinanzeigen.de, one or the other would certainly be happy...

Simply enter the ISBN number or scan it with a barcode scanner, the rest is automated.
For this purpose, a config.json file with the ads is generated. You can then use https://github.com/donwayo/ebayKleinanzeigen to read the configfile in and the advertisements are published.

----

Wir haben sehr viele Bücher und wussten nicht mehr wohin damit. Dann sagte meine Frau, wenn es nicht so aufwendig wäre, dann könnten wir sie bei ebay-kleinzeigen.de einstellen, bestimmt würde sich der eine oder andere freuen...

Einfach die ISBN Nummer eingeben oder mittels Barcode Scanner einscannen, der Rest geschieht automatisiert.
Dazu wird eine config.json Datei mit den Anzeigen generiert. Anschließend kann diese mit https://github.com/donwayo/ebayKleinanzeigen eingelesen und die Anzeigen veröffentlicht werden.

----

## Installation

1. follow the instructions on https://github.com/donwayo/ebayKleinanzeigen until it is up and running
2. download the script create_book_article_on_ebay_kleinanzeigen.py and place it in the same directory
3. configure some values in create_book_article_on_ebay_kleinanzeigen.py
- bookPrice = "1" for the default price, here 1€
- configure the ebayKleinanzeigen.py call on the last line:
  os.system("C:\\Users\\ulrik\\AppData\\Local\\Programs\\Python\\Python39\\python.exe kleinanzeigen.py --profile config.json")
4. start the script with "python create_book_article_on_ebay_kleinanzeigen.py"
