from selenium.webdriver.common.by import By
from behave import given, when, then


orders_icon = (By.ID, 'nav-orders')
sign_in = (By.XPATH, "//h1[@class='a-spacing-small']")
email_field = (By.ID, 'ap_email')
@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('click on orders icon')
def click_orders_icon(context):
    context.driver.find_element(*orders_icon).click()

@then('Verify that Sign in is shown')
def verify_sign_in_result(context):
    context.driver.find_element(*sign_in)

@then('Verify that email field is present')
def verify_email_field(context):
    context.driver.find_element(*email_field)

