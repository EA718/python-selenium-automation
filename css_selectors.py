from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='./chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()


# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')

# By CSS, using ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
