# Weekly Status Report 4 [February 8th, 2023]


## **Team Report**

#### **Past Week Goals**

-   Beta release - functional prototype with some mock data
-   Model - Have a functioning model endpoint with parsed string input that can reliably give a preset response on validity of text using a w&b table

#### **Progress Update**

-   Beta release complete, with functional frontend, model, and database connection established

#### **Following Week Goals**

-   Beta release - functional prototype with some mock data
    -  Model - Have a functioning model endpoint with parsed string input that can reliably give a preset response on validity of text using a w&b table

## **Contributions of Team Members**

#### **Past Week Goals**

Aditya: Prepare for beta release, fully integrate frontend prototype with backend, write additional tests for frontend prototype

Ayan: Continue working on finalizing firebase auth integration

Connor: Write more comprehensive example tests for model as we add data and filter the expected input. Finalize the endpoint communication to be able to get frontend info to backend to model and then back to the
website, completing our misinformation chain.

Danny: Finalize DB insert/query code in time for beta, write tests for eventual real data, solve GH Actions IP address problem

Sanjana: Add more to API and backend to finalize for beta release and demo. Write more backend tests.

#### **Current Week Contributions**

Aditya: Worked with Connor and Danny to finish integrating the frontend and backend in time for the beta release and wrote additional tests for the frontend api module.

Ayan: Made significant progress on getting the firebase AuthUI “out of the box” solution offered by google integrated into the frontend. Ended up shifting to a different style of integration after running into many issues trying to implement firebase with a custom backend.

Connor: Updated both readmes. Edited frontend URL to link to backend, and passed the correct request and header types to misinformation route. Connected frontend to backend, backend to model, model to DB. Improved model prompt and how model data is parsed. Fixed connection errors to the DB. Began research into more permanent website hosting.

Danny: Finalized DB code and all DB tests, solved IP whitelist problem for CI, added secret environment variables for database credentials preventing future URI key leaks.

Sanjana: Finalized backend for beta release–finalized relevant API endpoints and added and finalized API tests using PyTest.

#### **Next Week Planned Contributions**

Aditya: Build prototype of user history feature, write user and developer documentation.

Ayan: Finish up firebase auth integration by 2/22 to meet the timeline goals. Start working on how user “keys” will be passed from firestore to backend to correctly associate user history into in our DB.

Connor: Add fine-tuning to both prompt and model learning. Connect user history endpoint to the frontend. Figure out how to best store and then track a user throughout the website. Make decision on how to host backend site for final release.

Danny: Ensure backend/database can connect smoothly, and refactor/write new methods as needed. Write new tests for any additions. Ensure Firebase user authentication and database user id are managed properly and can interact. Write user and developer documentation, focusing specifically on anything pertaining to the database.

Sanjana: Work on user and development documentation. Specifically for the user documentation, how to run and use the software, and how to report a bug. Specifically for the developer documentation, the directory structure and how to build the software and add new tests to it.
