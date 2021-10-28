from django.db import models

# Create your models here.
class Services(models.Model):
    name= models.CharField(max_length=255)
    description= models.TextField()
    price=models.IntegerField()
    imgUrl=models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 