import csv  
import pandas as pd  

# define the path to the CSV file, this should be adjusted to your specific file location
csv_file = "path/to/your/sales_data.csv"

df = pd.read_csv(csv_file)

# identify duplicate rows based on the 'order_id' column
# the subset parameter specifies that duplicates are identified based on the 'order_id' column only
duplicate_rows = df[df.duplicated(subset='order_id')]

# print when duplicate rows are found in the CSV file 
print("Duplicate rows found in the CSV file:")
print(duplicate_rows)
