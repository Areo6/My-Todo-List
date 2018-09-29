## DESCRIPTION

Todo-List is a platform where people can add and manage their todo list

## Link to Todo-List on Github Pages

[To-do List App](https://eubule.github.io/My-To-do-App/)


## Routes captured by Todo-List

 REQUEST | ROUTE | FUNCTIONALITY
 ------- | ----- | -------------
 **POST** | /api/register | Creates a new User
 **POST** | /api/login | Logs the user in
 **GET** | /api/tasks | Fetches all tasks
 **POST** | /api/tasks | Posts an new task
 **PUT** | /api/tasks/< taskId> | Marks Task as Finished
 **DELETE** | /api/tasks/< taskId> | Deletes a task
 **DELETE** | /api/tasks | Deletes all tasks

## BUIT WITH

 * Flask-Python

## HOW TO RUN THE APPLICATION

 ### SETING UP THE ENVIRONMENT
 
 1. Clone this repository to your local PC

    **` git clone https://github.com/Eubule/My-Todo-List.git `** [here](https://github.com/Eubule/My-Todo-List)


 2. Create a virtual environment to run application specific dependencies

    **`$ virtualenv venv`**  To create a virtual environment separate from your system

    **`$ source venv/bin/activate`**   To activate you virtual environment

    **`$ pip install flask`**   To install the flask framework that will be used throughout

    **`$ pip freeze > requirements.txt`**   To install requirements useful when hosting the app on a remote server


 ### RUN THE APP

 1. To run the app

    **` python app.py `**

 2. To run tests

    **`  python -m pytest --cov app/ `**


## Author

**Malaba**