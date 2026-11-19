# One import of all librarys
import pandas as pd
import csv

# Load all the files
df  = pd.read_csv("03_Library Systembook.csv")
df1 = pd.read_csv("03_Library SystemCustomers.csv")
df2 = ""

# TEMP: Removing the problematic row
df.iloc[16]
df.drop(16, inplace=True)

rows = df.shape[0]
print(f"Number of rows: {rows}")

def clean(df_input):
   # Use Re (regular expressions) to 
   df_clean = df_input.copy()
   df_clean = df_clean.dropna()
   df_clean['Book checkout'] = df_clean['Book checkout'].str.strip('"')
   df_clean['Book checkout'] = pd.to_datetime(df_clean['Book checkout'], errors='coerce')
   df_clean['Book Returned'] = pd.to_datetime(df_clean['Book Returned'], errors='coerce')
   df_clean = df_clean.dropna(subset=["Book checkout", "Book Returned" ])
   df_clean['diff_days'] = (df_clean['Book Returned'] - df_clean['Book checkout']).dt.days
   return df_clean

# Try Except Block
try:
    # Clean file 1 via function 
    df_clean = clean(df_input=df)
except Exception as e:
    print(f"Error Occured: {e}")

# Clean file 2
df1 = df1.dropna()

rows1 = df_clean.shape[0]
print(f"Number of rows: {rows1}")

df3 = [rows,rows1]

with open('metrics.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([rows,rows1,rows-rows1])

# Output clean files
df_clean.to_csv("BooksClean.csv")
df1.to_csv("CustomersClean.csv")

