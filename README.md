# Users API
[![Build Status](https://app.travis-ci.com/HASSAN1A/my_users_api.svg?branch=main)](https://app.travis-ci.com/github/HASSAN1A/my_users_api) [![Coverage Status](https://coveralls.io/repos/github/HASSAN1A/my_users_api/badge.svg?branch=main)](https://coveralls.io/github/HASSAN1A/my_users_api?branch=main)

## Installation
  - Install [Python](https://www.python.org/downloads/), [Pip](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/), [Redis on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04) and [Postgres](https://www.postgresql.org/) on your machine
  - Clone the repository `$ git clone https://github.com/HASSAN1A/my_users_api.git`
  - Change into the directory `$ cd /my_users_api`
  - Installing virtualenv `$ python3 -m pip install --user virtualenv` command
  - Create the project virtual environment with `$ python3 -m venv env` command
  - Activate the virtual environment `$ source env/bin/activate`
  - Install all required dependencies with `$ pip install -r requirements.txt`
  - Export the required environment variables
      ```
      $ export FLASK_ENV=development
      $ export DATABASE_URL=postgres://name:password@localhost:port/polls
      $ export JWT_SECRET_KEY=your secret key
      ```
  - Start the app with `python3 run.py`


