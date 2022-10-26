from django.db import models

class CrudUser(models.Model):
    name = models.CharField(max_length = 80)
    address = models.CharField(max_length = 50)
    age = models.IntegerField()
    def __str__(self):
        return self.name


  





