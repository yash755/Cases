import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

mail_url = 'https://cpdocket.cp.cuyahogacounty.us'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())

driver.get(mail_url)

driver.find_element_by_id('SheetContentPlaceHolder_btnYes').click()



driver.find_element_by_id('SheetContentPlaceHolder_rbCrName').click()

time.sleep(5)

driver.find_element_by_id('SheetContentPlaceHolder_criminalNameSearch_txtLastName').send_keys('Smith')

driver.find_element_by_id('SheetContentPlaceHolder_criminalNameSearch_btnSubmitName').click()

time.sleep(5)