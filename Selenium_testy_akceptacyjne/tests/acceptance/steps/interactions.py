from behave import *

use_step_matcher('re')

@when('I click on the link with id "(.*)"')
def stem_impl(context, link_id):
    link = context.driver.find_element_by_id(link_id)
    link.click()