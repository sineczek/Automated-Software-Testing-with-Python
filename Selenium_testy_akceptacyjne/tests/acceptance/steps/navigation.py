import time

from behave import *
from selenium import webdriver

from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')  # pozwala "steps" otrzymać instrujkcję ze scenariusza gherkina


@given('I am on the homepage')
def stem_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(HomePage.url)  # testowo


@given('I am on the blog page')
def stem_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('http://127.1:5000/blog')


@then('I am on the blog page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    #time.sleep(2)
    assert context.driver.current_url == expected_url
