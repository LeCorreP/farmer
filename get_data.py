import os
import wget

# URL of the CSV file (replace with the actual CSV URL)
url = 'https://www.research-collection.ethz.ch/bitstreams/42a2f58b-d925-4352-908f-91db854466a1/download?accept=1'
csv_name = "data_raw.csv"

# Download the CSV file directly
wget.download(url, csv_name)

print(f"Downloaded: {csv_name}")

