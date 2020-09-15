
import requests
from os import path
import sources as so
from glob import glob
import functions as fun
from datetime import date

(PATH_O, nids, OVW) = (
        '/home/chipdelmal/Documents/CDC/docs/',
        ['DENV', 'CHIKV', 'ZIKV'], False
    )
# Cycle through the diseases URLs -----------------------------------------------
idsNum = len(nids)
fPaths = glob(PATH_O+'*.pdf')
(fNum, fNames) = (len(fPaths), fun.stripPaths(fPaths))
print('- Storing files to {}'.format(PATH_O))
for (i, nid) in enumerate(nids):
    # Get file URL --------------------------------------------------------------
    urlPdf = path.join(so.baseUrl, so.diseaseFile.get(nid))
    print('\t* ({}/{}) Downloading {} from {}'.format(i+1, idsNum, nid, urlPdf))
    # Check if file already exists ----------------------------------------------
    today = date.today()
    outFName = '{}_{}'.format(nid, str(today)[:-3])
    outFPath = '{}/{}.pdf'.format(PATH_O, outFName)
    outFExists = path.exists(outFPath)
    # Download and save PDF -----------------------------------------------------
    if (not outFExists or OVW):
        # Request the PDF from url ----------------------------------------------
        response = requests.get(urlPdf)
        # Write to disk ---------------------------------------------------------
        with open(outFPath, 'wb') as f:
            f.write(response.content)
print('- Finished!')
