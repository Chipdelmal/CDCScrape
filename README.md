# CDPH Scrape

These scripts were created to scrape the monthly California Department of Public Health (CDPH) arbovirus case updates to CSV files for easy analysis.

* [pdfDownload.py](./pdfDownload.py): Downloads PDFs defined in [sources.py](./sources.py) to a directory.
* [pdfScrape.py](./pdfScrape.py): Scrapes the PDFs looking for tables and getting rid of parentheses data and notes (redundant to counts).

##  Use

Currently, paths need to be changed 'in-file' but I'll add a wrapper in the near future to call the whole thing from bash.
To parse the tables from the PDFs run the scripts as follows (making sure the `PATH_O` from `pdfDownload` matches `PATH_I` in `pdfScrape`):

```
python pdfDownload.py
python pdfScrape.py
```

##  Dependencies

To install the required dependencies, run:

```bash
pip install camelot-py pandas
```

## Authors

<img src='https://raw.githubusercontent.com/Chipdelmal/MK8DLeaderboard/master/media/pusheen.jpg' height="130px" align="middle"><br>

[Héctor M. Sánchez C.](https://chipdelmal.github.io/blog), [Tomás León](https://tomasleon.com/)
