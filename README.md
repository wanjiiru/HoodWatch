# Hoodwatch
[Wanjiiru](https://github.com/wanjiiru) 

## Description
Neighbourhood Watch is a web app that allows you to view neighbourhoods, join neighbourhoods and create businesses and posts in their neighbourhoods


## Specifications
- Admin Panel that allows adding locations and their descriptions.
- Search Feature to enable searching locations.
- Show date location was posted.

## Setup/Installation Requirements

### Clone the Repo
Run the following command on the terminal:
- git clone https://github.com/wanjiiru/HoodWatch.git && cd Neigh

### Activate virtual environment

Activate virtual environment using python3.6 as default handler

```sh
virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
```

### Install dependencies

Install dependencies that will create an environment for the app to run

```sh
pip3 install -r requirements.txt
```

### Create the Database

```sh
psql
CREATE DATABASE neigh;
```

### .env file
Create .env file and paste paste the following filling where appropriate:

```python
SECRET_KEY = '<Secret_key>'
DBNAME = ''
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
```

### Run initial Migration
```sh
python3.6 manage.py makemigrations
python3.6 manage.py migrate
```

### Run the app
```sh
python3.6 manage.py runserver
```
#### Open terminal on
```sh
localhost:8000
```

## Known Bugs
  -No known bugs, recommendations on improvements and on known bugs will be appreciated. 

## Technologies used

```sh
- Python 3.6.5
- Django MVC framework
- HTML, CSS and Bootstrap
- Postgressql
- Heroku
```

## Support and contact details
 - Email Address: liz240@live.com

## Link to deployed site
[HoodWatch](https://hoodliz.herokuapp.com/) 


## License and terms of use

[MIT License](license) this application's source code is free for any open source projects



 © Wanjiiru | Credits [Moringa School](https://moringaschool.com/)
