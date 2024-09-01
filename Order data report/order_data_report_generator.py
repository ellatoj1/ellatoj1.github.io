import pandas as pd  
import os  
import pprint  # importing pprint for pretty-printing of data structures (optional)

path1 = os.path.join(os.path.dirname(__file__), 'order_data_1.csv')
path2 = os.path.join(os.path.dirname(__file__), 'order_data_2.csv')
path3 = os.path.join(os.path.dirname(__file__), 'customer_details.csv')

order_data_1 = pd.read_csv(path1)
order_data_2 = pd.read_csv(path2)
customer_details = pd.read_csv(path3)

# rename the column 'client_id' to 'customer_id' in order_data_2 to ensure consistency
order_data_2.rename(columns={'client_id': 'customer_id'}, inplace=True)

# combine the two order datasets into a single DataFrame
combined_orders = pd.concat([order_data_1, order_data_2], ignore_index=True)
print('\ncombined_orders:\n', combined_orders)

# merge the combined orders with customer details based on 'customer_id'
merged_data = pd.merge(combined_orders, customer_details, on='customer_id', how='left')

# remove any duplicate rows based on 'order_id', keeping the first occurrence
merged_data.drop_duplicates(subset='order_id', keep='first', inplace=True)

# handle NaN values separately for numerical and string columns
numerical_cols = merged_data.select_dtypes(include=['float64', 'int64']).columns
string_cols = merged_data.select_dtypes(include=['object']).columns
merged_data[numerical_cols] = merged_data[numerical_cols].fillna(0)  # fill NaN in numerical columns with 0
merged_data[string_cols] = merged_data[string_cols].fillna('')  # fill NaN in string columns with an empty string

# convert all dates to a consistent format (year-month-day)
# 'coerce' converts invalid dates to NaT (Not a Time)
merged_data['order_date'] = pd.to_datetime(merged_data['order_date'], errors='coerce')
merged_data['order_date'] = merged_data['order_date'].dt.strftime('%Y-%m-%d')

# convert any invalid dates to NaT
merged_data['order_date'] = merged_data['order_date'].fillna(pd.NaT)

# define a function to calculate the average price per product in an order
def calculate_avg_price(row):
    product_count = len(row['product_list'].split(',')) if row['product_list'] else 0
    return row['total_price'] / product_count if product_count > 0 else 0

# apply the function to calculate the average product price for each order
merged_data['average product price'] = merged_data.apply(calculate_avg_price, axis=1)
print('\nmerged_data:\n', merged_data)

# sort the data based on 'total_price' in descending order
sorted_data = merged_data.sort_values(by='total_price', ascending=False)
print('\nsorted_data:\n', sorted_data)

# define the output path for the Excel file. Replace this with your desired file path
output_path = os.path.join(os.path.dirname(__file__), 'output.xlsx')

# write the merged data to an Excel file with a cover sheet
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    merged_data.to_excel(writer, index=False, sheet_name='Output')

    workbook = writer.book
    worksheet = writer.sheets['Output']

    header_format = workbook.add_format({'bold': True})
    for col_num, value in enumerate(merged_data.columns.values):
        worksheet.write(0, col_num, value, header_format)

    # create a cover sheet with basic information about the document contents
    front_sheet = workbook.add_worksheet('Försättsblad')
    front_sheet.write('A1', 'Innehåll på dokumentet:')
    front_sheet.write('A2', 'Denna fil innehåller data om ordrar med följande kolumner:')
    for i, column in enumerate(merged_data.columns):
        front_sheet.write(i+2, 0, f"{column}: Beskrivning av kolumnens innehåll.")
