from django.contrib import admin

# after models.py
from home.models import Contact
#register your model here
# now they find in admin panel
admin.site.register(Contact)

#after that go to apps.py find app name, here home is our app
# go to settings .py and add it to installed apps
# 'home.apps.HomeConfig',

#after that command line
# python manage.py makemigrations
# python manage.py migrate
