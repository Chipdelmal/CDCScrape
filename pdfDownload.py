

import requests
from datetime import date


nid = 'ZIKV'
url = 'https://www.cdph.ca.gov/Programs/CID/DCDC/CDPH%20Document%20Library/'
urlPdf = url + 'TravelAssociatedCasesofZikaVirusinCA.pdf'
out = './docs/'
# Request the PDF from url
response = requests.get(url)
# Write to disk
today = date.today()
with open('./docs/{}_{}.pdf'.format(nid, str(today)[:-3]), 'wb') as f:
    f.write(response.content)
