# Polygraph Backend

# User Manual

## Polygraph Project Goals
Our project is a website where users can input text (such as facts or news) and check it for accuracy. We will fine tune a GPT-3 model to evaluate the accuracy of inputted text, and provide users with an evaluation of whether their text is accurate or not, along with an explanation of why. Our workflow will look something like this: a user logs in to the fact checker website using their credentials. Once they log in, they see a text box where they can input text and receive an evaluation of its accuracy. They can also view their history (which is their previously inputted text along with the corresponding evaluations).

### Features:
1. User accounts. Users will be able to create accounts with which they can use to gain access to our website fact checker.

   i.  Non-operational: Firebase login authentication system not yet implemented.

2. False text detection. Once users log in, they can input text and receive an evaluation of its accuracy along with an explanation of the evaluation.

   i.  Operational: Fully connected enpoints with feedback, although not trained on dataset.

3. Text validation. The text that users input will be vetted and verified for acceptable language and profanity to encourage result accuracy.

   i.  Operational: Maximum query length and profanity filter have been implemented.

4. User history. Once users log in with their credentials, they can view their history of previous inputted text along with the corresponding accuracy evaluations.

   i.  Non-operational: Database can store and interact with user history, but endpoint to UI not implemented.

## Setup
1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. If you don't have conda installed, [install it from here](https://conda.io/projects/conda/en/stable/user-guide/install/download.html)

3. Clone this repository

4. Navigate into the project directory

   ```bash
   $ cd polygraph
   ```

5. Create the conda environment:
   ```bash
   $ conda create --name polygraph python=3.10.0
   $ conda activate polygraph
   ```

6. Install the requirements from requirements.txt
   ```bash
   $ pip install -r requirements.txt
   ```

7. Make a copy of the example environment variables and example pytest.ini file
   ```bash
   $ cp .env.example .env
   $ cp pytest.ini.example pytest.ini
   ```

8. Add your [openAI key](https://beta.openai.com/account/api-keys) and [MongoDB username + password](https://www.mongodb.com/docs/cloud-manager/tutorial/enable-mongodbcr-authentication-for-group/) to the newly created `.env` and `pytest.ini` files
   - Note for purposes of peer review: Message Connor Lynch (clynch20@uw.edu) on Slack or via email for the OpenAI and DB keys


## Starting the Flask Application
1. Make sure you have cloned and are running the [polygraph backend](https://github.com/sanjanachin/polygraph)

2. Run the app locally using the following command:
   ```bash
   $ flask run
   ```

## Reporting a bug
Report all bugs as GitHub issues.

## Known bugs
Known bugs can be found [here](https://docs.google.com/document/d/1YKue4Q9jE8VMdDHGTT1DMFyiaw8GF5UWjrJQ4gYJcew/edit?usp=sharing).

<br />

# Developer Guidelines

## Prerequisites
See the above User Manual above for instructions on installing/running the software and reporting bugs.

## Obtaining source code
All of the source code for the polygraph backend can be found in this repo. The source code for the polygraph UI can be found [here](https://github.com/sanjanachin/polygraph-ui).

## Project Structure:
Polygraph Directory Contents:
- tests/:
   - test_app.py - basic endpoint pytest suite for the backend
   - test_db.py - basic endpoint pytest suite for the database
   - test_app.py - basic post request pytest suite for the backend
- reports/: directory that stores the group weekly status reports
- app.py - python Flask route API for frontend, model, and database
- db.py - mongoDB database module methods
- requirements.txt - the necessary requirements for client installation
- .env.example - the skeleton code for a unique .env creation
- pytest.ini.example - the skeleton code for a unique pytest.ini creation

## Testing
### To run existing tests
Test suites can be run from the command line with the following command:
   ```bash
   $ pytest
   ```
This will run all test suites within the tests/ directory

### To add new tests
To add a new test to the codebase, you can either add a test to one of the existing test files or create a new test file.

- If adding to an existing test file, add a new function in the test file with the following format:
```
def name_of_test(self):
    {test body goes here}
```
   - Note that the test name in the function header must start with 'test' (e.g., `test_healthcheck`, `test_misinformation`, etc)

- If creating a new test file, create a file in the `/tests` directory with this format:
```
import pytest
class name_of_class:
```
   - Then, follow the steps above for adding to an existing test file to add a new unit test to your new test file.
   - Note that the test file’s name must start with 'test' (e.g., `test_app.py`, `test_db.py`, etc)
   
## Building a release 
To build a new release of polygraph, commit the changes associated with the new release and use a Git tag to tag the release with the new version number. 
