Travis CI stats [![Build Status](https://travis-ci.org/misraX/django_iban.svg?branch=master)](https://travis-ci.org/misraX/django_iban)

## Installation:

1- Create new directory:

`mkdir iban`

2- Move to the new directory:

`cd iban`

3- Create a new python2 virtualenv:

`virtualenv venv -p /bin/python2`

or

`virtualenv $("which python2") venv`

4- Activate the new virtualenv:

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
# for test dependinces and development.
pip install -r requirements/dev.txt
```

8- Migrate to create the new database:

`./manage.py migrate`

9- Load initial data to setUp Google account and
   Google related auth configuration
   
`./manage.py loaddata socialaccounts.json`

10- Create superUser Just for the admin page use cases, **Its not required**:

`./manage.py createsuperuser`

11- Run Djano Development server and open `localhost:8000` in your browser:

`./manage.py runserver`

12- Login Using your Google account.

13- After login Google will redirect you to the home page `/`

14- You can Add a new user account from the top or go to `localhost:8000/iban/add/`.

15- After successfully adding a new user the page will redirect you to the instance page `localhost:8000/<instance_id>`
    
16- Logout from the top right next to Add User IBAN.

17- Login with another Google account.

18 - You will redirect to the home page again `/`.

19- You will see the instance that you previously created but no actions buttons Update nor Delete will
    be available, it is only allowed for the owner of the instance.    

20- Create a new instance using the same method in number 14, it will redirect you to the new instance page same as number 15.

21- Go to the home page `localhoost:8000` or from the left menu `USERS ACCOUNT LIST` you will find your new instance in the table list, 
    with the actions buttons Update and Delete, and the other instances will be available but without update or delete actions.

### Available project URLs:

`/` iban ListView, List all IBANAccount instances.

`/iban/<pk>` iban DetailView, Detail View of the requested <pk> instance.

`/iban/update/<pk>` iban UpdateView, Update View of the requested <pk> instance. (only for the user who created the instance)

`/iban/delete/<pk>` iban DeleteView, Delete View of the requested <pk> instance POST request only. (only for the user who created the instance)

`/iban/add/` iban CreateView, Create a new IBANAccount instance.

### Docs:

[Code Reference](http://django-iban.readthedocs.io/en/latest/py-modindex.html "ReadTheDocs")


### Tests, TDD:

Travis Continuous Integration: [Travis CI](https://travis-ci.org/misraX/django_iban)

Locally: Simply install `dev.txt` requirements and
`./manage.py test`

The project originally created with `python 2.7.14`

Python versions passed the tests:

    - "2.7"
    - "3.4"
    - "3.5"
    - "3.5-dev"
    - "3.6"
    - "3.6-dev"


### ScreenShots:

`./iban_screenshots`

### Notes:

1. Its important for Google auth to run the server using localhost:8000.
2. The website is only allowed for logged in administrators...
3. `apps.iban.auth.mixins.PreventManipulationAccessMixin` is a custom `AccessMixin` prevents manipulation operations.
4. For a close code reference check [Code Reference](http://django-iban.readthedocs.io/en/latest/py-modindex.html "ReadTheDocs").

### Third party apps and Credits goes to:

1. [Ligh BootStrap Dashboard] (https://github.com/creativetimofficial/light-bootstrap-dashboard "LightBoatStrapDashBoard").
2. [django-allauth](https://github.com/pennersr/django-allauth "allauth") for social integrations.
3. [django-localflavor](https://github.com/django/django-localflavor "localflavor") for Coutnry specific helpers.
