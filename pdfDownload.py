

import requests
from datetime import date
from selenium import webdriver


(nid, PATH_O) = ('ZIKV', '/home/chipdelmal/Documents/CDC/docs/')
url = 'https://www.cdph.ca.gov/Programs/CID/DCDC/CDPH%20Document%20Library/'
urlPdf = url + 'TravelAssociatedCasesofZikaVirusinCA.pdf'

# Request the PDF from url
response = requests.get(urlPdf)
# Write to disk
today = date.today()
with open('{}/{}_{}.pdf'.format(PATH_O, nid, str(today)[:-3]), 'wb') as f:
    f.write(response.content)
