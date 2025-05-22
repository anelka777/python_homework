from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://owasp.org/www-project-top-ten/")
driver.implicitly_wait(10)
list_items = driver.find_elements(By.XPATH, "//li[a[contains(@href, 'Top10')]]")

results = []
for item in list_items:
    try:
        link_element = item.find_element(By.TAG_NAME, "a")
        title = link_element.text.strip()
        href = link_element.get_attribute("href")
        results.append({"Title": title, "Link": href})
    except Exception as e:
        print(f"Error processing item: {e}")
        continue

driver.quit()

df = pd.DataFrame(results)
df.to_csv("owasp_top_10.csv", index=False)

for entry in results:
    print(f"{entry['Title']}: {entry['Link']}")
