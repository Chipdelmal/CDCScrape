
import ntpath
import camelot
import pandas as pd
from glob import glob
import functions as fun

(PATH_I, PATH_O) = (
        '/home/chipdelmal/Documents/CDC/docs/',
        '/home/chipdelmal/Documents/CDC/tables/'
    )
fNames = glob(PATH_I+'*.pdf')
fName = 'TravelAssociatedCasesofZikaVirusinCA.pdf'
for fName in fNames:
    # Load file and parse tables ----------------------------------------------
    tables = camelot.read_pdf(fName, pages='1-end')
    print("Total tables extracted:", tables.n)
    # Cleanup the table -------------------------------------------------------
    dfs = [fun.cleanupDF(table) for table in tables]
    # Merge dataframes --------------------------------------------------------
    dfPre = pd.concat(dfs).dropna()
    dfPst = dfPre.apply(lambda x: x.str.replace('\n', ''))
    dfPst.to_csv(PATH_O+ntpath.basename(fName)[:-4]+'.csv')
