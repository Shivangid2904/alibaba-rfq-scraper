from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


driver = webdriver.Chrome()


base_url = "https://sourcing.alibaba.com/rfq/rfq_search_list.htm?spm=a2700.8073608.rfqSearch.list.1.82be65aaoUUItC&country=AE&recently=Y&tracelog=newest&page={}"

data = []


for page in range(1, 101):
    url = base_url.format(page)
    driver.get(url)
    
    time.sleep(5)

    rfqs = driver.find_elements(By.CLASS_NAME, 'brh-rfq-item__container')

    for rfq in rfqs:
        try:
            title = rfq.find_element(By.CLASS_NAME, 'brh-rfq-item__subject-link').text.strip()
        except:
            title = ""

        try:
            quantity = rfq.find_element(By.CLASS_NAME, 'brh-rfq-item__quantity-num').text.strip()
        except:
            quantity = ""

        try:
            country = rfq.find_element(By.CLASS_NAME, 'brh-rfq-item__country').text.strip()
        except:
            country = ""

        try:
            date_posted = rfq.find_element(By.CLASS_NAME, 'brh-rfq-item__publishtime').text.strip()
        except:
            date_posted = ""

        try:
            buyer_name = rfq.find_element(By.CLASS_NAME, 'text').text.strip()
        except:
            buyer_name = ""

        data.append({
            'Title': title,
            'Quantity Required': quantity,
            'Country': country,
            'Date Posted': date_posted,
            'Buyer Name': buyer_name
        })

    print(f"Scraped page {page}")


driver.quit()

df = pd.DataFrame(data)
df.to_csv('alibaba_rfqs.csv', index=False)

print("Data scraped and saved to alibaba_rfqs.csv")
