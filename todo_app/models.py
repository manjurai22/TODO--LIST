from django.db import models

# Create your models here.

#If there is any change in models.py run following:
#python manage.py makemigrations
#python manage.py migrate

class Todo(models.Model): #PascalCase
    title=models.CharField(max_length=200) #varchar,char

    def __str__(self): 
        return self.title