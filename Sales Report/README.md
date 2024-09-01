# Sales Data Processing System

## Overview

This system is designed to import and process sales data from a CSV file, analyze the data, and generate a structured and comprehensive Excel report with calculations and visual representations. The primary goal is to enable users to easily understand and present sales patterns and regional differences in a professional and efficient manner.

## User Story

As a **system user**, I want to be able to:

- **Import Sales Data**: 
  - Read a CSV file containing sales data with columns such as date, product name, quantity, and price.
  - Handle different delimiters, including commas and semicolons.

- **Data Validation and Error Handling**: 
  - Validate that all necessary columns are present and that the data is in the correct format before processing begins.
  - Provide clear error messages if any data issues are detected, allowing for corrections before further processing.

- **Data Conversion and Sorting**: 
  - Convert date strings to date format.
  - Sort sales data in ascending order based on date.

- **Excel Workbook Creation**: 
  - Create a new Excel workbook with separate worksheets for sales data and regional summaries.
  - Name and organize these worksheets according to specific requirements.

- **Total Sales Calculation**: 
  - Automatically calculate and add a column for total sales (quantity * price) in the sales worksheet.
  - Format numeric values appropriately, such as currency and thousand separators.

- **Regional Sales Summary**: 
  - Summarize sales by region and create a summary table on a separate worksheet.
  - Ensure the table is clearly formatted and easy to read.

- **Chart Generation**: 
  - Generate a bar chart that visually represents sales by region.
  - Include correctly labeled axes, labels, and a title on the chart.
  - Place the chart on the same worksheet as the regional sales summary.

- **File Handling**: 
  - Save the generated Excel file to a specified path.
  - Allow the option to overwrite existing files or create a new file if necessary.

- **Error Handling and User Feedback**: 
  - Handle errors, including missing or incorrect data, and provide clear instructions for resolving issues.
  - Halt the process if critical errors are encountered.

## Technical Specifications

- **CSV Handling**: 
  - The system will utilize a flexible CSV parser capable of handling various delimiters.

- **Excel Workbook Management**: 
  - The system will use a library that supports the creation and management of Excel files in .xlsx format, such as OpenPyXL or Pandas.

- **Error Management**: 
  - The system will implement robust error handling and exception management, ensuring the process can continue if errors are non-critical or halts if necessary.

## How to Use

1. **Import CSV Data**: Place the CSV file in the designated location and ensure it contains the required columns: date, product name, quantity, and price.
2. **Run the System**: Execute the script or application. The system will validate the data, process it, and generate the required Excel file.
3. **Review Output**: Once the process is complete, locate the Excel file in the specified directory and review the data, summaries, and charts.

## Installation

To install and run this system, ensure you have the following dependencies installed:

- Python 3.x
- Pandas library
- OpenPyXL library

Install the required Python packages using pip:

```bash
pip install pandas openpyxl

