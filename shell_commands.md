## Common Shell Commands

### Django Shell

'''bash
python manage.py shell
'''

### Django Settings

__Accessing global variables/config in 'settings.py'__
'''python
from django.conf import settings

MY_VAR = getattr(settings, 'MY_VAR', 'default')
API_KEY = getattr(settings, 'API_KEY', None)
'''

__Debug__
'''python

DEBUG = settins.DEBUG
'''

__BASE_DIR__
'''python

BASE_DIR = settings.DEBUG
'''

### Import of a Model

'from <appname>.models import <ClassName>'

'''python
from emails.models import EmailEntry
'''

### Get a single stored item

'''python
EmailEntry.objects.get(id=1)
# example of using get while returning more than one thing, cant  do that
# EmailEntry.objects.get(email="devinrowland12@gmail.com")
'''

### List all stored items of a Model
'''python
# list of model instances that are stored in the database
EmailEntry.objects.all()
'''

### Filter all stored items of a Model
'''python
EmailEntry.objects.filter(email="devinrowland12@gmail.com")
'''

### Create a new stored item (instance) of a model
'''python
EmailEntry.objects.create(email='devin@dova.com')
'''
or
'''python
obj = EmailEntry()
obj.email='devin@dova.com'
obj.save()
'''

### Update a new stored item (instance) of a Model
'''python
obj = EmailEntry.objects.get(id=1)
obj.name = "Devin"
obj.save()
'''

### Delete a new stored item (instance) of a Model
'''pyhton
obj = EmailEntry.objects.get(id=5)
obj.delete()
'''