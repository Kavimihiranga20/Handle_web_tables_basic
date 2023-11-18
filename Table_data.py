from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

driver.get("https://www.w3schools.com/html/html_tables.asp")

wait = WebDriverWait(driver, 5)

table = wait.until(EC.presence_of_element_located((By.ID, "customers")))

rows = table.find_elements(By.TAG_NAME, 'tr')

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")

    for cell in cells:
        print(cell.text)


