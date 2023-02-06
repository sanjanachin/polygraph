# Polygraph Backend

## Polygraph Project Goals
Our project is a website where users can input text (such as facts or news) and check it for accuracy. We will fine tune a GPT-3 model to evaluate the accuracy of inputted text, and provide users with an evaluation of whether their text is accurate or not, along with an explanation of why. Our workflow will look something like this: a user logs in to the fact checker website using their credentials. Once they log in, they see a text box where they can input text and receive an evaluation of its accuracy. They can also view their history (which is their previously inputted text along with the corresponding evaluations).

### Features:
1. User accounts. Users will be able to create accounts with which they can use to gain access to our website fact checker.
2. False text detection. Once users log in, they can input text and receive an evaluation of its accuracy along with an explanation of the evaluation.
3. Text validation. The text that users input will be vetted and verified for acceptable language and profanity to encourage result accuracy.
4. User history. Once users log in with their credentials, they can view their history of previous inputted text along with the corresponding accuracy evaluations.

### Project Structure:
Main Directory Contents:
- app.py - the main python flask route API
- requirements.txt - the necessary requirements for client installation
- apihandler:
  - FrontEndApiHandler.py - the api handler for the UI interface (react)
  - ModelApiHandler.py - the api handler for the model (gpt-3)

### To create conda environment:
```
conda create --name polygraph python=3.10.0
conda activate polygraph
pip install -r requirements.txt
```

### To run the app:
```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

To run on Windows:
```
set FLASK_APP=app
set FLASK_ENV=development
flask run
```

### To run the tests: 
```
pytest tests
```

