# Disaster Response Pipeline


This project involves working with a figure8 disaster response dataset, to build and deploy a machine learning classifier, to classify messages to reach their respective disaster response departments.

![Screenshot](screen.png)

## Installations

Following libraries were used (preinstalled):

pandas
numpy
nltk
sklearn- 0.19.1
sqlalchemy
pickle
re
##Project components:
The project consists of three components

### 1. ETL Pipeline

Explore the database provided by figure8
Clean the database and distribute the columns for eact category
Make a SQL DB file

### 2. ML Pipeline

Use the DB created in the last step 
Build a ML pipeline using multioutput classifer
Use grid search to find the best parameters 
Save the model as a pickel file

### 3. Flask web app

Use the Flask library to host the project
Use the Templates provided by Udacity for the front-end of the system
use the pickel file to load the model and classify the messages 


## Run the App Locally 
execute the following command to the command promt or terminal from the app directory.

**python3 app.py**

you need to have all the libararies installed beforing running the app.

File structure:
Here's the file structure of the project:

###app

| - template

| |- master.html # main page of web app

| |- go.html # classification result page of web app

|- app.py # Flask file that runs app
|- classifier.pkl
|- myfirstsql.db


###data

|- disaster_categories.csv # data to process

|- disaster_messages.csv # data to process

|- process_data.py

|- DisasterResponse.db # database to save clean data to

###models

|- train_classifier.py

|- classifier.pkl # saved mode


Acknowledgements
Data has been provided by Figure Eight

Tutorials from Pandas and Sklearn were used developing the code:

http://pandas.pydata.org/
http://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
http://scikit-learn.org/stable/modules/model_evaluation.html#classification-report
http://scikit-learn.org/stable/modules/classes.html#module-sklearn.ensemble
Along with lessons in the Udacity Data Science Nanodegree

Software engineering (Pandas and Flask)
Data engineering (ETL, NLP, ML Pipelines)

Project By Inamul Haq
