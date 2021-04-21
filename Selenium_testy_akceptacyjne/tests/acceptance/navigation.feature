Feature: test navigation between aps
  Behavior Driven Development BDD

  Scenario: Homepage can go to Blog
    Given I am on the homepage
    When I click on the link with id "blog-link"
    Then I a on the home page