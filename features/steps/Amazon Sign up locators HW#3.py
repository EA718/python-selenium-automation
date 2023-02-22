#Amazon logo
#By CSS, using class
#driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')

#Create account
#By CSS, using class
#driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

#Name field
#driver.find_element(By.ID, 'ap_customer_name')

#Email field
#driver.find_element(By.ID, 'ap_email')


#Password field
#driver.find_element(By.ID, 'ap-password')

#Passwords must be at least 6 characters.
#driver.find_element(By.Xpath, "//div[contains(text(), 'Passwords must be at least 6 characters.')]")

#Reenter password field
#driver.find_element(By.ID, 'ap-password_check')

#Continue link
#driver.find_element(By.ID, 'continue')

#Conditions of Use
#driver.find_element(By.Xpath, "//a[contains(@href, ap_register_notification_condition_of_use')]")

#Privacy notice
#driver.find_element(By.Xpath, "//a[contains(@href, ap_register_notification_privacy_notice')]")
