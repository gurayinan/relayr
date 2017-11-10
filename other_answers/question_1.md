### Question :
Imagine the following situation.You need to establish a QA process in a cross-functional team.The team builds a front-end application using REST APIs.
#### Sub Question 1 :
Where would you start? What would be your first steps?
#### Answer :
- As a first step, I would check the documentation to have a general idea of the REST API itself.
- Then I would create sample test cases based on features and the required parameters and go over those cases to make them detailed as good as possible so we can cover as much as cases related to that REST API possible. (Assuming that REST API is already tested while in development, if not we need to test the REST API itself beforehand.)
- If there are automated tests related to the API then I would check them against my cases to make sure we are not missing any points in test cases.If not then after cross-check with test cases written by other team members we can automate those cases to make API test coverage better.
- Later on, I would check-in with the team members responsible for front-end part of the application to check if they have a sample that can be tested (for ex. sample page with mock data) and plan front-end automation tests accordingly.

#### Sub Question 2 :
Which process would you establish around testing new functionality? How would you  want the features to be tested?  
#### Answer :
- For testing new features I would start with a standard sanity / smoke test which aims to make sure that all major functions are working properly and version is ready for detailed tests.With that way we can avoid spending too much effort beforehand.
- Afterwards if first checks are successful I would prepare a functionality test (Before you need to read the documents related to feature of course.) with custom input data to check what the outcome is looking like.If the outcome is expected than I can move onto next step.
- As a last step for testing new feature before making sure it is ready for a release I would do a verification test as well.For example if the feature is expected to store data into some database or make file operations then I would check those on the systems we are conducting tests upon to make sure everything is working correctly.
- Note 1: If the feature that is being tested is also system / hardware specific than those steps could be altered with a system requirements check as well.
- Note 2: After every release I would try to create a separate environment with latest release so that I can make an exploratory test as well. (Without any test script or plan just try to find errors or bugs related to system with minimal knowledge about the system / software itself)

#### Sub Question 3 :

Which tools would you suggest using to help your team with a daily work?

#### Answer :
- Postman for executing requests to REST APIs etc. easily
- JIRA or Trello for tracking sprint status in Agile teams (Scrum or Kanban)
- Locust for performing stress tests.
- Apache JMeter for performance / load tests as well as recording test cases for native apps.

#### Sub Question 4 :
If you would do a test automation which techniques or best practices would you use the application?

#### Answer :
- When writing test cases for test automation always prefer to use unique controllers first if applicable. (for ex. use ID property of a web element before using XPATH since XPATH can be changed easily on any kind of frontend update like element shift)
- Only automate cases which are repetitive for multiple builds, prone to human error, dependent on multiple datasets or takes too much effort to do it manually.
- Another important point is to prepare good test data and update it.If there is an option you can always prepare mock data from real data taken from application itself. (Replacing or removing essential / critical information)
- Always aim for fast results on automation systems. (run multiple test cases at the same time if they do not affect one other for ex.)