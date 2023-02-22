from selenium.webdriver.common.by import By
from behave import given, when, then

cart_icon = (By.ID, 'nav-cart-count-container')
amazon_cart_is_empty = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2")
expected_result = "Your Amazon Cart is empty"

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(*cart_icon).click()

@then('Verify that Your Amazon cart is empty is shown')
def verify_amazon_cart_is_empty_result(context):
    context.driver.find_element(*amazon_cart_is_empty)

@then('Verify that text {expected_result} is shown')
def verify_expected_result(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'