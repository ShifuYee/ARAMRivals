# ARAM Rivals
### ARAM stats tracker, most recent match analyzer

## Setup for development
We want to install Pipenv through with homebrew:

`brew install pipenv`

because of the following reasons: https://pipenv.readthedocs.io/en/latest/

1. Create a new virtual environment by running:

`pipenv --three`

2. Install Django and Django REST framework by running:

`pipenv install django djangorestframework`

3. After installation ends, spawn a shell within the virutal environment by running:

`pipenv shell`

python will refer to python3 when executing commands

# Database Info

To clear the database:

1. `psql`

2. `drop database "insert_database_name";`

3. `create database "insert_database_name";`

4. go to migrations folder in "server/leads/migrations/" and delete all files except __init__.py

To recreate the tables and fill in with fixtures:

5. `python manage.py makemigrations leads`

6. `python manage.py migrate`

7. `python manage.py loaddata leads`

# Tech
1. React
  + Babel
  + Webpack
2. Django
3. PostgreSQL
