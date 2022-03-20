# My Users API

[![Build Status](https://app.travis-ci.com/HASSAN1A/my_users_api.svg?branch=main)](https://app.travis-ci.com/github/HASSAN1A/my_users_api) [![Coverage Status](https://coveralls.io/repos/github/HASSAN1A/my_users_api/badge.svg?branch=main)](https://coveralls.io/github/HASSAN1A/my_users_api?branch=main)

![alt text](app.png)
## Video Demonstration

[![Watch the video](https://i.imgur.com/vKb2F1B.png)](https://youtu.be/8L-cHQT0uQc)


## Description
This is a flask multi-user REST API endpoint backend application where a user can sign up,log in get a a token and consume backend service using the provided endpoints.

## For detailed API Endpoints Overview click [ API Documentation](https://github.com/HASSAN1A/my_users_api/blob/main/APIDOCUMENTATION.md).
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
     7. [Mockaroo](https://www.mockaroo.com/)  
## Installation and Set-up
Here is a run through of how to set up the application:
  
  - Clone the repository `$ git clone https://github.com/HASSAN1A/my_users_api.git`
  - Go to the project root directory and  create a virtual environment. Run the following commands respectively: `$ cd /my_users_api`
  - Installing virtualenv `$ python3 -m pip install --user virtualenv` command
  - Create the project virtual environment with `$ python3 -m venv venv` command
  - Activate the virtual environment `$ source venv/bin/activate`
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
    * You will see a landing page with a sign up and log in form.
## Contribution in Development
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 

## Bug / Feature Request



If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/HASSAN1A/my_users_api/issues/new) by including your search query and the expected result.
If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/HASSAN1A/my_users_api). Please include sample queries and their corresponding results.

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request

## Built with

1. [Python 3.8](https://www.python.org/doc/) : Programming language.
2. [Flask](https://flask.palletsprojects.com/en/1.1.x/): Framework used.
3. [HTML](https://www.w3schools.com/html/) : Layout.
4. [CSS](https://www.w3schools.com/css/) : Styling.
5. [Bootstrap](https://mdbootstrap.com/) : For responsive websites.
6. [posgreSQL](https://www.postgresql.org/) : Database language.
7. [psycopg2](https://pypi.org/project/psycopg2/) : Database driver.
8. [JWT](https://jwt.io/) : Authentication.
9. [Docker](https://www.docker.com/) : For running the application.
10. [Heroku](https://www.heroku.com/) : For deploying the application.
11. [Git](https://git-scm.com/) : Version control.
12. [GitHub](github.com) : For hosting the repository.
13. [Postman](https://www.getpostman.com/) : For testing the API.
14. [Figma](https://www.figma.com/file/xvfDjQAeSMTPAhz1mkkgl9/myusersapikata?node-id=0%3A1) - Blueprint for designing the web app.

## To-do

- To work on any issue that may arise,maintain the site and allow others to pair programme with me by raising their comments/issues that so that we work on them to achieve a common goal .

## Team

[Hassan Juma ](https://github.com/HASSAN1A)

## [License](https://github.com/HASSAN1A/my_users_api/blob/main/LICENCE.md)

[MIT](https://github.com/HASSAN1A/my_users_api/main/LICENSE.md) © [Hassan Juma](https://github.com/HASSAN1A)