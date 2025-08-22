import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

SRC_URL = ""

def prep_webpages(base_url):
	webpages = []

	# code to prepare the list of webpages to comb through
	webpages.append(base_url)

	return webpages 


serv = ChromeService(ChromeDriverManager().install())
opt = webdriver.ChromeOptions()

#opt.add_argument("--headless")
opt.add_argument("--no-sandbox")
opt.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(service=serv, options=opt)


webpages = prep_webpages(SRC_URL)

for url in webpages:
	browser.get(url)

	wait = WebDriverWait(browser, 10)

	text_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/main/section[1]/div/div/div/h1")))
	print(text_element.text)

	#img_element = wait.until(EC.visibility_of_element_located((By.XPATH, "full XPATH of HTML element")))
	#print(img_element.get_attribute("src"))

time.sleep(2)
browser.quit()
