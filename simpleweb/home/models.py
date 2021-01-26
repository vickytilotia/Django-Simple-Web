from django.db import models

# Create your models here.
# trying to save contact form data
# after creating model go to admin.py and register it there.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.IntegerField()
    desc =models.TextField()