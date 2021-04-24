import time

from behave import *
from selenium import webdriver

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')  # pozwala "steps" otrzymać instrujkcję ze scenariusza gherkina


@given('I am on the homepage')
def stem_impl(context):
    context.driver = webdriver.Chrome()
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('I am on the blog page')
def stem_impl(context):
    context.driver = webdriver.Chrome()
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    print(context.driver.current_url)
    print(expected_url)
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    print(context.driver.current_url)
    print(expected_url)
    assert context.driver.current_url == expected_url
