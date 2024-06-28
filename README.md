# bipartisan-etf
A parody portfolio that combines NANC &amp; KRUZ Subersive ETFs

# Some Notes
- Currently only analyzes common stocks.
# How to run your own
1. Download pdfs from https://www.subversiveetfs.com/nanc and https://www.subversiveetfs.com/kruz with holdings date you're interested in analyzing.
2. Use https://www.ilovepdf.com/ to convert the PDFs so that OCR can recognize it better.
3. Use https://convertio.co/pdf-csv/ to convert PDF to CSV.
4. (optional) Clean up the top and bottom part of text file that has some legal technalities. See `10-80-NANC-N-PORT-Part-F-123123-V5-Confidential.csv`.

Now you can either modify `merge_etfs.py` python file or work with Jupyter Notebook. Refer to `conda_env.txt` so you can import the environment get working right away on Anaconda.

# Contribution
All PR submissions welcome.

- Are there keywords other than PLC(a), Inc. etc that the script is not filtering properly? Feel free to edit merge_etfs.py conditional statements that filter them out. 
- What's the correlation between two ETFs like?
- And any other insights are welcome.