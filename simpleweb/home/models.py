from django.db import models

# Create your models here.
# trying to save contact form data
# after creating model go to admin.py and register it there.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.IntegerField()
    desc =models.TextField()


    def __str__(self):
        # it will display the contact name in django admin contact list
        # instead of object1, object1
        return self.name
    