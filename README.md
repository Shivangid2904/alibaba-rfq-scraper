# Alibaba RFQ Web Scraper

This is a Python-based web scraper that extracts Request for Quotation (RFQ) data from Alibaba’s sourcing portal using Selenium. The scraped data is saved into a CSV file.

##  Features
- Scrapes RFQ listings from the first 100 pages
- Extracts:
  - Title
  - Quantity Required
  - Country
  - Date Posted
  - Buyer Name
- Saves all data into a CSV file (`alibaba_rfqs.csv`)
##  Technologies Used
- Python 3
- Selenium
- Pandas
- Google Chrome & ChromeDriver
##  How to Run
1. **Install the required libraries:**
   ```bash
   pip install selenium pandas
Download ChromeDriver (compatible with your Chrome version):
https://sites.google.com/chromium.org/driver/
Place chromedriver.exe in your project folder (or add it to PATH).
Run the script:
bash
python scraper.py
Output:
A file named alibaba_rfqs.csv will be created in the same directory.

Files Included
scraper.py: Python script containing the web scraping logic
alibaba_rfqs.csv: The scraped data in CSV format

Notes:
A 5-second delay is added (time.sleep(5)) to ensure pages load fully before scraping.
The CSV structure was designed based on the fields available on the website.
