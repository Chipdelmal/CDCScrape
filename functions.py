
import ntpath
import pandas as pd
pd.options.mode.chained_assignment = None


def selectPaths(USR):
    (pthDocs, pthTbls) = ('./docs/', './tables/')
    if (USR == 'chipdelmal'):
        (pthDocs, pthTbls) = (
                '/home/chipdelmal/Documents/CDC/docs/',
                '/home/chipdelmal/Documents/CDC/tables/'
            )
    if (USR == 'srv'):
        (pthDocs, pthTbls) = (
                '/RAID5/marshallShare/CDPH/docs/',
                '/RAID5/marshallShare/CDPH/tables/'
            )
    return (pthDocs, pthTbls)

def cleanCell(cell):
    clean = str(cell).replace('\n', '')
    clean = clean.split(' ')[0]
    clean = ''.join(filter(str.isdigit, clean))
    return clean


def cleanupDF(table):
    df = table.df
    # Read and clean column names
    title = df.iloc[0]
    years = [i.split('\n')[-1] for i in title[1:]]
    labels = [title[0]]
    labels.extend(years)
    # Changing column names
    df.columns = labels
    # Deleting first row (now column names)
    df = df[1:]
    # Setting the first column as index
    cleanCounty = df['County'].map(lambda x: x.replace('\n', ''))
    df['County'] = cleanCounty
    df = df.set_index(df.columns[0])
    # Delete 'Total' row
    if (df.index == 'Total').any():
        df = df.drop('Total')
    # Return cleaned up DF
    return df

def stripPath(fPath, ext='.pdf'):
    return ntpath.basename(fPath).replace(ext, '')


def stripPaths(fPaths, ext='.pdf'):
    return [stripPath(fPath) for fPath in fPaths]
