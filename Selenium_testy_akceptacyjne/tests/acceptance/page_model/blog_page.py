from tests.acceptance.locators.blog_page import BlogPageLocators
from tests.acceptance.page_model.base_page import BasePage


class BlogPage(BasePage):
    @property
    def url(self):
        return super(BlogPage, self).url + '/blog'

    @property
    def post_section(self):
        return self.driver.finf_element(*BlogPageLocators.POST_SECTION)

    @property
    def post(self):
        return self.driver.finf_element(*BlogPageLocators.POST)

    @property
    def add_post_link(self):
        return self.driver.finf_element(*BlogPageLocators.ADD_POST_LINK)