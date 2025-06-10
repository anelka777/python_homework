from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os
import json

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

time.sleep(5)

search_results = driver.find_elements(By.TAG_NAME, "li")
print(f"Search result: {len(search_results)}")

search_results = driver.find_elements(By.CLASS_NAME, "cp-search-result-item")

results = []

for item in search_results:
    try:
        title_element = item.find_element(By.CLASS_NAME, "title-content")
        title = title_element.text.strip()

        author_elements = item.find_elements(By.CLASS_NAME, "author-link")
        authors = "; ".join([a.text.strip() for a in author_elements])

        format_info_div = item.find_element(By.CLASS_NAME, "cp-format-info")
        format_info_span = format_info_div.find_element(By.TAG_NAME, "span")
        format_year = format_info_span.text.strip()

        results.append({
            "Title": title,
            "Author": authors,
            "Format-Year": format_year
        })

    except Exception as e:
        print(f"Error: {e}")
        continue

df = pd.DataFrame(results)
print(df)

driver.quit()

csv_path = "get_books.csv"
df.to_csv(csv_path, index=False)

json_path = "get_books.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("The data saved into the files:")
print(f"- CSV: {csv_path}")
print(f"- JSON: {json_path}")
