# Polygraph Backend

## Polygraph Project Goals
Our project is a website where users can input text (such as facts or news) and check it for accuracy. We will fine tune a GPT-3 model to evaluate the accuracy of inputted text, and provide users with an evaluation of whether their text is accurate or not, along with an explanation of why. Our workflow will look something like this: a user logs in to the fact checker website using their credentials. Once they log in, they see a text box where they can input text and receive an evaluation of its accuracy. They can also view their history (which is their previously inputted text along with the corresponding evaluations).

### Features:
1. User accounts. Users will be able to create accounts with which they can use to gain access to our website fact checker.
2. False text detection. Once users log in, they can input text and receive an evaluation of its accuracy along with an explanation of the evaluation.
3. Text validation. The text that users input will be vetted and verified for acceptable language and profanity to encourage result accuracy.
4. User history. Once users log in with their credentials, they can view their history of previous inputted text along with the corresponding accuracy evaluations.

### Project Structure:
Polygraph Directory Contents:
- apihandler/:
   - FrontEndApiHandler.py - the api handler for the UI interface (react)
   - ModelApiHandler.py - the api handler for the model (gpt-3)
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

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd polygraph
   ```

4. Create the conda environment:
   ```bash
   $ conda create --name polygraph python=3.10.0
   $ conda activate polygraph
   ```

5. Install the requirements from requirements.txt
   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables and example pytest.ini file
   ```bash
   $ scp .env.example .env
   $ scp pytest.ini.example pytest.ini
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. (Optional) Add your [API key](https://beta.openai.com/account/api-keys) to the `pytest.ini` file. This will let you properly run pytest with the test_model suite.

## To run the app:

   ```bash
   $ flask run
   ```

##  To run the tests:

   ```bash
   $ pytest
   ```
