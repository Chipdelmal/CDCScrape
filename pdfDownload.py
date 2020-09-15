

import requests
import sources as so
from datetime import date

(PATH_O, nids) = (
        '/home/chipdelmal/Documents/CDC/docs/',
        ['DENV', 'CHIKV', 'ZIKV']
    )
# Cycle through the diseases URLs -----------------------------------------------
idsNum = len(nids)
print('- Storing files to {}'.format(PATH_O))
for (i, nid) in enumerate(nids):
    # Get file URL --------------------------------------------------------------
    urlPdf = so.baseUrl + so.diseaseFile.get(nid)
    print('\t* ({}/{}) Downloading {} from {}'.format(i+1, idsNum, nid, urlPdf))
    # Request the PDF from url --------------------------------------------------
    response = requests.get(urlPdf)
    # Write to disk -------------------------------------------------------------
    today = date.today()
    with open('{}/{}_{}.pdf'.format(PATH_O, nid, str(today)[:-3]), 'wb') as f:
        f.write(response.content)
print('- Finished!')
