
import re
import ntpath
import camelot
import pandas as pd
from glob import glob
import functions as fun

(PATH_I, PATH_O) = (
        '/home/chipdelmal/Documents/CDC/docs/',
        '/home/chipdelmal/Documents/CDC/tables/'
    )
# Cycle through the PDFs -------------------------------------------------------
fNames = glob(PATH_I+'*.pdf')
fNum = len(fNames)
print('- Storing files to {}'.format(PATH_O))
for (i, fName) in enumerate(fNames):
    # Load file and parse tables -----------------------------------------------
    tables = camelot.read_pdf(fName, pages='1-end')
    # print("Total tables extracted:", tables.n)
    print('\t* ({}/{}) Processing {}'.format(i+1, fNum, fName))
    # Cleanup the table --------------------------------------------------------
    dfs = [fun.cleanupDF(table) for table in tables]
    # Merge dataframes ---------------------------------------------------------
    dfPre = pd.concat(dfs).dropna()
    dfPst = dfPre.applymap(fun.cleanCell)
    dfPst.to_csv(PATH_O+ntpath.basename(fName)[:-4]+'.csv')
print('- Finished!')
