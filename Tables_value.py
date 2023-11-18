import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

driver.get("https://demoqa.com/webtables")

wait = WebDriverWait(driver, 5)

button = wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton")))
button.click()
firstName = wait.until(EC.presence_of_element_located((By.ID, "firstName")))
firstName.send_keys("Jhon")
lastName = wait.until(EC.presence_of_element_located((By.ID, "lastName")))
lastName.send_keys("123")
email = wait.until(EC.presence_of_element_located((By.ID, "userEmail")))
email.send_keys("jjhdb@gmail.com")
age = wait.until(EC.presence_of_element_located((By.ID, "age")))
age.send_keys("12")
salary = wait.until(EC.presence_of_element_located((By.ID, "salary")))
salary.send_keys("2000000")
department = wait.until(EC.presence_of_element_located((By.ID, "department")))
department.send_keys("ICT department")
submitBtn = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
submitBtn.click()

button = wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton")))
button.click()
firstName = wait.until(EC.presence_of_element_located((By.ID, "firstName")))
firstName.send_keys("Mike")
lastName = wait.until(EC.presence_of_element_located((By.ID, "lastName")))
lastName.send_keys("788993")
email = wait.until(EC.presence_of_element_located((By.ID, "userEmail")))
email.send_keys("khsdjw@gmail.com")
age = wait.until(EC.presence_of_element_located((By.ID, "age")))
age.send_keys("18")
salary = wait.until(EC.presence_of_element_located((By.ID, "salary")))
salary.send_keys("6000000")
department = wait.until(EC.presence_of_element_located((By.ID, "department")))
department.send_keys("ICT department")
submitBtn = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
submitBtn.click()

table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "rt-table")))
rows = table.find_elements(By.CLASS_NAME, "rt-tr-group")

for row in rows:
    cells = row.find_elements(By.CLASS_NAME, "rt-td")
    cellText = cells[1].text.strip()
    textCharsCount = len(cellText)

    if textCharsCount > 0:
        if cellText.isnumeric():
            cells[6].find_element(By.CLASS_NAME, "action-buttons").find_elements(By.TAG_NAME, "span")[0].click()
            time.sleep(5)
            wait.until(EC.presence_of_element_located((By.ID, "lastName"))).clear().send_keys("new last name")
            time.sleep(1)
            wait.until(EC.presence_of_element_located((By.ID, "submit"))).click()
            time.sleep(10)





