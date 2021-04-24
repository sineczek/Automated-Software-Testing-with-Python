Feature: test navigation between aps
  Behavior Driven Development BDD

  Scenario: Homepage can go to Blog
    Given I am on the homepage
    When I click on the "Go to blog" link
    Then I am on the blog page


  Scenario: Homepage can go to Homepage
    Given I am on the blog page
    When I click on the "Go to home" link
    Then I am on the homepage