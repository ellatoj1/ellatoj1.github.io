# Job Scraping and Data Storage Project

## Overview

This project involves scraping job listings from the website [Real Python Fake Jobs](https://realpython.github.io/fake-jobs/), organizing the collected data into a structured format, ensuring consistent data formatting, and storing the final dataset in a JSON file.

## User Story

As a **data engineer**, I want to scrape the website `https://realpython.github.io/fake-jobs/`, organize the collected job information into a list of dictionaries, ensure that each location is correctly formatted, and save the results to a JSON file so that the information is well-organized, consistent, and easily accessible for further analysis and use.

## Acceptance Criteria

- The website `https://realpython.github.io/fake-jobs/` should be successfully scraped to collect job listings, including job title, company, location, and posting date.
- The collected job information should be stored in a list of dictionaries, where each dictionary contains the following keys: `title`, `company`, `location`, and `date_posted`.
- Location names should be formatted correctly, with the first letter capitalized and the remaining letters in lowercase. Special cases should be handled appropriately.
- The final list should be saved to a JSON file named `job_search_v2.json`, which should be well-formatted and easy to read and validate.
- The JSON file should be written in UTF-8 format and placed in a specified directory, with proper handling of any existing files with the same name (either overwriting or versioning based on configuration).

## Technical Specifications

- The script should use Python libraries such as `BeautifulSoup` or `Scrapy` for web scraping and the `json` module in Python to write the results to a file.
- All data handling should include robust error handling to ensure that unexpected situations are managed without causing the script to crash.
- There should be test cases to verify that the script handles various scenarios, including inconsistent data and location names with different formats.



