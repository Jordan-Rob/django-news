simple django app incorporating:
-custom user model
-authentication
-authorization and permissions
-foreignkey usage within models
for frontend:
-crispy forms
-bootsrap cdn
-whitenoise to handle stattic files within heroku

to test it out online visit https://dj-news.herokuapp.com/

steps for usage
within your terminal / command prompt

1.run "git clone https://github.com/Jordan-Rob/django-news"

2. cd into the directory in which you have cloned the repo and
   run "pipenv install" (if you do not have pipenv install it via the "pip install pipenv" command)
   this will enable you install the dependencies from the pipfile

3. enter your virtual environment with command "pipenv shell"

4. run "py manage.py runserver" to test it out locally
