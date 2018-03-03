Travis CI stats [![Build Status](https://travis-ci.org/misraX/django_iban.svg?branch=master)](https://travis-ci.org/misraX/django_iban)

## Installation:

1- Create new directory:

`mkdir iban`

2- Move to the new directory:

`cd iban`

3- Create a python2 virtual enviroment:

`virtualenv -p /bin/python2 venv`

4- Activate the new virtuenv:

`source venv/bin/activate`

5- Clone the repository as django_iban:

`git clone git@github.com:misraX/django_iban.git django_iban`

6- Move to django_iban:

`cd django_iban`

7- Install project dependencies:

```
# for base dependinces
pip install -r requirements/base.txt
```

```
# for test dependinces and base.
pip install -r requirements/dev.txt
```

8- Migrate to create the new database:

`./manage.py migrate`

9- Load initial data to setUp Google account and
   Google related auth configuration
   
`./manage.py loaddata socialaccounts.json`

10- Create superUser:

`./manage.py createsuperuser`

11- Run Djano Development server:

`./manage.py runserver`

12- Open localhost:8000 in your browser.


### Available project URLs:

`/` iban ListView, List all IBANAccount instances.

`/iban/<pk>` iban DetailView, Detail View of the requested <pk> instance.

`/iban/update/<pk>` iban UpdateView, Update View of the requested <pk> instance.

`/iban/delete/<pk>` iban DeleteView, Delete View of the requested <pk> instance POST request only.

`/iban/add/` iban CreateView, Create a new IBANAccount instance.

### Docs:

[Code Reference](http://django-iban.readthedocs.io/en/latest/py-modindex.html "ReadTheDocs")


### Tests:

Simply install `dev.txt` requirements and
`./manage.py test`

Python versions passed the tests:

    - "2.7"
    - "3.4"
    - "3.5"
    - "3.5-dev"
    - "3.6"
    - "3.6-dev"

The project originally created with `python 2.7.14`

### ScreenShots:

`./iban_screenshots`

### Notes:

1. Its important for Google auth to run the server using localhost:8000.
2. Update and Delete views are only available if request.user is the same user who created the requested model instance. 