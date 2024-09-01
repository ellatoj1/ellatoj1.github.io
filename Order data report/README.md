# README: Order Data Processing and Export

## Description

This project is designed to process and combine order data from multiple sources, integrate it with customer details, and ensure that the data is clean and consistent. The processed data is then exported as a well-documented Excel file that can be shared with others for further analysis.

## User Story

**As a data analyst**, I want to be able to process and combine order data from multiple sources, integrate it with customer details, and ensure the data is clean and consistent, so that I can export the results as a well-documented Excel file to share a complete and analyzable dataset with my colleagues.

## Acceptance Criteria

- **Data Import and Combination:**
  - Order data from `order_data_1` and `order_data_2` should be imported and combined into a unified table without any data loss.
  - The combined order table should be further merged with the `customer_details` table based on a common key (e.g., customer ID).

- **Data Quality:**
  - Duplicate rows in the combined table should be identified and removed.
  - All cells containing NaN values should be filled with an empty string (`""`).
  - Dates in the table should be converted to a consistent format (e.g., `YYYY-MM-DD`).

- **Data Analysis and Sorting:**
  - The rows in the table should be sorted in ascending or descending order based on the total price.
  - A new column, `average product price`, should be created by dividing the total order value by the number of products in each order.

- **Export to Excel:**
  - The final combined and processed table should be saved as an Excel file using pandas.
  - The headers in the Excel file should be formatted in bold for clarity.
  - A cover sheet should be included in the Excel file explaining the content, column descriptions, and other relevant metadata.
  - The Excel file should be saved with a name that reflects its content and purpose for easy identification.

