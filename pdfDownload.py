

import requests
import sources as so
from datetime import date
from selenium import webdriver


(nid, PATH_O) = ('CHIKV', '/home/chipdelmal/Documents/CDC/docs/')
# Get file URL ------------------------------------------------------------------
urlPdf = so.baseUrl + so.diseaseFile.get(nid)
# Request the PDF from url ------------------------------------------------------
response = requests.get(urlPdf)
# Write to disk -----------------------------------------------------------------
today = date.today()
with open('{}/{}_{}.pdf'.format(PATH_O, nid, str(today)[:-3]), 'wb') as f:
    f.write(response.content)
