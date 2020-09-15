
import re
import ntpath
import camelot
import pandas as pd
from glob import glob
import functions as fun

(PATH_I, PATH_O, OVW) = (
        '/home/chipdelmal/Documents/CDC/docs/',
        '/home/chipdelmal/Documents/CDC/tables/',
        True
    )
# Cycle through the PDFs -------------------------------------------------------
fPaths = glob(PATH_I+'*.pdf')
(fNum, fNames) = (
        len(fNames),
        [ntpath.basename(fName).replace('.pdf', '') for fName in fNames]
    )
print('- Storing files to {}'.format(PATH_O))
for (i, fPath) in enumerate(fPaths):
    print('\t* ({}/{}) Processing {}'.format(i+1, fNum, fPath))
    outFPath = PATH_O+fNames[i]+'.csv'
    # Load file and parse tables -----------------------------------------------
    outFExists = os.path.exists(outFPath)
    if (not outFExists or OVW):
        # Cleanup the table ----------------------------------------------------
        tables = camelot.read_pdf(fPath, pages='1-end')
        dfs = [fun.cleanupDF(table) for table in tables]
        # Merge dataframes -----------------------------------------------------
        dfPre = pd.concat(dfs).dropna()
        dfPst = dfPre.applymap(fun.cleanCell)
        dfPst.to_csv(outFName)
print('- Finished!')
