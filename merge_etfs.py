import re
import csv

NANC_CSV_FILE = "10-80-NANC-N-PORT-Part-F-123123-V5-Confidential.csv"
KRUZ_CSV_FILE = "11-81-KRUZ-N-PORT-Part-F-123123-V5-Confidential.pdf-00-48-16-852.csv"

NANC_STOCKS = set()
KRUZ_STOCKS = set()
with open(NANC_CSV_FILE, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        number_filter = re.search("[0-9]+(\.[0-9]+)?%", row[0]) # don't need lines with just with numbers
        # print(row)
        if not (number_filter) and (
                "Inc" in row[0] or 
                "Corp" in row[0] or 
                "Co" in row[0] or 
                "PLC" in row[0] or
                "ADR" in row[0] or
                "Ltd" in row[0] or
                "AG" in row[0] or
                "Bancorp" in row[0]
                ):
            row[0] = re.sub(r'[\x00-\x1f]+', '', row[0]) # cleanup: replaces \xad or \xad\x0c by nothing
            if re.search(" {2,}", row[0]):
                # ['Silgan Holdings, Inc.                                      44           1,991']
                # cleanup: for these kind of rows where there's ridiculous amount of spacing due to table view
                row[0] = re.sub('[0-9,,,.,§]', '', row[0])
                row[0] = row[0].strip()
                #print(row)
                NANC_STOCKS.add(row[0])
            else:
                #print(row)
                NANC_STOCKS.add(row[0])

# print(NANC_STOCKS)

with open(KRUZ_CSV_FILE, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        number_filter = re.search("[0-9]+(\.[0-9]+)?%", row[0]) # don't need lines with just with numbers
        # print(row)
        if not (number_filter) and (
                "Inc" in row[0] or 
                "Corp" in row[0] or 
                "Co" in row[0] or 
                "PLC" in row[0] or
                "ADR" in row[0] or
                "Ltd" in row[0] or
                "AG" in row[0] or
                "Bancorp" in row[0]
                ):
            row[0] = re.sub(r'[\x00-\x1f]+', '', row[0]) # cleanup: replaces \xad or \xad\x0c by nothing
            if re.search(" {2,}", row[0]):
                # ['Silgan Holdings, Inc.                                      44           1,991']
                # cleanup: for these kind of rows where there's ridiculous amount of spacing due to table view
                row[0] = re.sub('[0-9,,,.,§]', '', row[0])
                row[0] = row[0].strip()
                #print(row)
                KRUZ_STOCKS.add(row[0])
            else:
                #print(row)
                KRUZ_STOCKS.add(row[0])

# print(NANC_STOCKS.intersection(KRUZ_STOCKS))
# print(NANC_STOCKS - KRUZ_STOCKS)
# print(KRUZ_STOCKS - NANC_STOCKS)


## Export to CSV etc