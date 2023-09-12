from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = ChromeOptions()
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://mail.google.com/')
