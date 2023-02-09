# Weekly Status Report 4 [February 8th, 2023]


## **Team Report**

#### **Past Week Goals**

-   Determine our CI service of choice via thorough group discussion/evaluation
of the pros and cons of various available options

-   Design a formal test plan - including unit, integration, and system testing as appropriate
    -   Identify the infrastructure of our test plan
    -   Set up and design our extensive testing plan
    -   Create example tests for each test type
    -   Repeat this process for each of our 5 main components



#### **Progress Update**

-   Set up working CI system with GitHub Actions

-   Created initial tests for Front end, back end, database, and model

#### **Following Week Goals**

-   Beta release - functional prototype with some mock data
    -  Model - Have a functioning model endpoint with parsed string input that can reliably give a preset response on validity of text using a w&b table

## **Contributions of Team Members**

#### **Past Week Goals**

Aditya: Contribute to testing/CI documentation, set up Github Actions (CI/CD) for frontend app, finish functional prototype of frontend

Ayan: Help with implementation of CI and automation infrastructure, specifically for DB 

Connor: Decide on CI, finish handler endpoints, create rough test shell with examples

Danny: Help with deciding on a CI service and help implement it, with a focus on front end/DB

Sanjana: Research different CI services and choose one. Choose test automation infrastructure. 

#### **Current Week Contributions**

Aditya: Contribute to testing/CI documentation, set up Github Actions (CI/CD) for frontend app, finish functional prototype of frontend

Ayan: Started working towards firebase integration for next weeks beta release goals. Set up firebase auth permissions. 

Connor: Generated openAI key and updated scripts with Actions - began fetching model info, started initial vetting of data and parse style features, imported (empty) w&b table

Danny: Initial setup of the DB, created some mock data for testing, wrote some initial tests and created methods for retrieving data

Sanjana: Researched and chose to use GitHub actions as CI service, and set up CI for backend repo. Wrote tests for backend/API which are run via CI every time anything is pushed to the repo. Added to API. Contributed to testing/CI documentation.



#### **Next Week Planned Contributions**

Aditya: Prepare for beta release, fully integrate frontend prototype with backend, write additional tests for frontend prototype

Ayan: Continue working on finalizing firebase auth integration 

Connor: Write more comprehensive example tests for model as we add data and filter the expected input. Finalize the endpoint communication to be able to get frontend info to backend to model and then back to the 
website, completing our misinformation chain.

Danny: Finalize DB insert/query code in time for beta, write tests for eventual real data, solve GH Actions IP address problem

Sanjana: Add more to API and backend to finalize for beta release and demo. Write more backend tests. 

