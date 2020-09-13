

import requests
from datetime import date
from selenium import webdriver


nid = 'ZIKV'
url = 'https://www.cdph.ca.gov/Programs/CID/DCDC/CDPH%20Document%20Library/'
urlPdf = url + 'TravelAssociatedCasesofZikaVirusinCA.pdf'
out = './docs/'
DRV = './chromedriver/chromedriver'


prefs = {
        "download.default_directory": out,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.plugins_disabled": ["Chrome PDF Viewer"],
        "plugins.always_open_pdf_externally": True
    }
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=DRV, chrome_options=options)
# Request the PDF from url
response = requests.get(url)
# Write to disk
today = date.today()
with open('./docs/{}_{}.pdf'.format(nid, str(today)[:-3]), 'wb') as f:
    f.write(response.content)
