# Python Testing / Coverage Measurement / Gherkin Test Specs

The code sample uses Unit testing and coverage measurement.

It is used to show problematics like measure 100% coverage while no single useful unit test assertion was executed.
Another code example shows how 100% coverage is achieved with some unit test assertions in place.
The Positive Functional test ran but does this mean we provided and selected the unit tests well?
Finally additional test types get introduced covering that here Boundary Testing, Sanity Testing, Negative Functional Testing is done.
The we are using Gherkin for Test Specs in Python comments. This will enable Test or Code Reviewers to compare
implemented functional code with test code and the test specification.

Does it support and help in a software development process?

The solution shows a low effort approach to be used for software development, doesn't it?

# Install / Usage

```
python --version
```

You should have a current version of Python 3 installed. At time of writing this README e.g. Python 3.13.1 is available.

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pdm update
run.cmd
```

That should now show no missed statements and 100% coverage in each test suite.
Now have fun studying the Python files.

# Test types

To get an idea on test types here are some:

* Unit Testing (Actual vs. Expected comparison)

The majority of test types below can be formulated as Unit Tests.
So talking about just Unit Testing is not helpful at all.
It should be specified what exact test type is intended in any Unit Test.
Unit Test just means an actual value is compared towards an expected value.
But it does not state anything whether that test intends to test e.g. value boundary issues,
sanity of values passed to the test in terms of fullfillment of a protocol on an API,
checking conformance of an architecture or simply functional testing as a positive test
using proven valid values compared to an expected return value, etc.
As such it is more helpful to use e.g. the following test types for refined specification.

* Functional Testing
    * Positive Test
    * Negative Test
* Load Testing
* Stability Testing
* Performance Testing
* Security Testing
* Safety Testing
* Integration Testing
* Contract Testing
* Architecture Conformance Testing
* Usability Testing
* Compatibility Testing
* Regression Testing
* Sanity Testing
* Boundary Testing
* Accessibility Testing
* System Testing
* User Acceptance Testing
* Non Functional Testing
* Quality Assurance Testing
* API Testing
* AB Testing (Version A vs. Version B given to peer group (users))
* Globalization Testing
* Internationalization Testing
* Compliance Testing
* Exploratory Testing
* Automation Testing
* Smoke Testing

# The Gherkin Part in the Code Comments

Gherkin language can be used e.g. to describe test sepcifications or acceptance criteria.
Gherkin is a language with just a few keywords actually.
Typical keywords used to start a line with are

* Feature:
* Scenario:
* Given
* When
* Then
* And

Some more Gherkin keywords exist but anyway these can be used as a good starting point.
An example usage of Gherkin from one of the tests in this repository is

```
        Feature: Add negative numbers representing sizes of a shape
        Scenario: Get the sum of two negative numbers

        Given I have two negative numbers representing sizes of a shape
        When I add them together
        Then I should get the a NaN value
```

Mind that you can incorporate SCRUM agile user stories in a Gherkin context as well.
User stories usually follow a schema like

“As [a user persona], I want [to perform this action] so that [I can accomplish this goal].”

Combined in Gherkin this can be formulated as

```
        Given I have two positive numbers
        When I add them together as a user of the function
        Then I should get the sum of the two numbers in order to...
```

```
        Given I have two positive numbers
        When [to perform this action] as [a user persona]
        Then I should get the sum of the two numbers in order to [accomplish this goal]
```
