from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='./chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-orders').click()

expected_text = 'Sign in'
actual_text = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

assert actual_text == expected_text, f'Expected {expected_text} but got actual {actual_text}'

# Verify email field present
assert driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'

driver.quit()
