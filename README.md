# My Users API

[![Build Status](https://app.travis-ci.com/HASSAN1A/my_users_api.svg?branch=main)](https://app.travis-ci.com/github/HASSAN1A/my_users_api) [![Coverage Status](https://coveralls.io/repos/github/HASSAN1A/my_users_api/badge.svg?branch=main)](https://coveralls.io/github/HASSAN1A/my_users_api?branch=main)

![alt text](ap.png)

## Description
This is a flask multi-user REST API endpoint backend application where a user can sign up,log in get a a token and consume backend service using the provided endpoints.


#### Live link : [link](https://hassanblog.herokuapp.co/)






## Consumer/User Stories

- POST /api/v1/users - create a user
- GET /api/v1/users - get all registered users
- GET /api/v1/users/<user_id> - get a user by id
-  GET /api/v1/users/me - get their info
- PUT /api/v1/users/me - update my account
- DELETE /api/v1/users/me - Delete my account

## Test Driven Development (TDD)

Test driven development is an iterative development process.

In TDD, developers write a test before they write just enough production code to fulfill that test and the subsequent refactoring. Developers use the specifications and first write test describing how the code should behave. It is a rapid cycle of testing, coding, and refactoring.

## Features

Here are the summary:

- A landing page showing Sign Up and Log In   form
- user is authenticated and able to consume the API after authentication.





## Requirements

- This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
## Installation
   - Install: 
     1. [Python](https://www.python.org/downloads/)
     2. [Pip](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/)
     3. [Redis](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04)
     4. [Docker](https://docs.docker.com/engine/install/ubuntu/)
     5. [Postgres](https://www.postgresql.org/) 
      6. [Flask](https://flask.palletsprojects.com/en/1.1.x/install/)
## Installation and Set-up
Here is a run through of how to set up the application:
  
  - Clone the repository `$ git clone https://github.com/HASSAN1A/my_users_api.git`
  - Go to the project root directory and  create a virtual environment. Run the following commands respectively: `$ cd /my_users_api`
  - Installing virtualenv `$ python3 -m pip install --user virtualenv` command
  - Create the project virtual environment with `$ python3 -m venv env` command
  - Activate the virtual environment `$ source env/bin/activate`
    * Note that you can exit the virtual environment by running the command **`deactivate`**
  - Install all required dependencies with `$ pip install -r requirements.txt`
  - Create the Database
    * - psql
    * - CREATE DATABASE yourdb;
  - Export the required environment variables
      ```
      $ export FLASK_ENV=development
      $ export DATABASE_URL=postgres://name:password@localhost:port/yourdb
      $ export JWT_SECRET_KEY=your secret key
      ```Or you can create a .env file and export the variables in it.
  - Run the application `$ flask run`

  - Start the app with `python3 run.py`
    * Open your preferred browser and view the app by opening the link **http://127.0.0.1:5000/**.


