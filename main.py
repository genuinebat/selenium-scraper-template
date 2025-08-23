import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

SRC_URL = "https://www.selenium.dev/documentation/"

def prep_webpages(base_url):
	webpages = []

	# code to prepare the list of webpages to comb through
	src_pages = ["overview", "webdriver", "selenium_manager"]
	for page in src_pages:
		webpages.append(base_url + page + "/")

	return webpages 


serv = ChromeService(ChromeDriverManager().install())
opt = webdriver.ChromeOptions()

#opt.add_argument("--headless")
opt.add_argument("--no-sandbox")
opt.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(service=serv, options=opt)

webpages = prep_webpages(SRC_URL)
webpages_headers = ["content"]
webpages_data = []

for url in webpages:
	browser.get(url)
	wait = WebDriverWait(browser, 10)

	data = []

	# code to extract the required information on each page
	text_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div/main/div/div[1]")))
	data.append(text_element.text)

	#img_element = wait.until(EC.visibility_of_element_located((By.XPATH, "full XPATH of HTML element")))
	#data["img"] = img_element.get_attribute("src")

	webpages_data.append(data)

with open("data.csv", "w", newline="") as csvf:
	writer = csv.writer(csvf)

	writer.writerow(webpages_headers)

	for data in webpages_data:
		writer.writerow(data)

time.sleep(2)
browser.quit()
