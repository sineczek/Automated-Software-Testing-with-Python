from behave import *

use_step_matcher('re') #re regular expressions

@when('I click on the link with id "(.*)"') # "(.*)" birze z feature to co jest w ""  . - dowolny znak * - dowolna ilość
def stem_impl(context, link_id):
    link = context.driver.find_element_by_id('blog-link')
    link.click()