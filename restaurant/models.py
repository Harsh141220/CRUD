from django.db import models
from django.db.models.fields import CharField

class food(models.Model):
    name= models.CharField(primary_key=True,max_length=150)
    des=models.TextField()
    cuisine=models.CharField(max_length=150 ,default="Indian")
    dat=models.DateField(auto_now=True)
    radio=models.CharField(max_length=150 ,default="Veg")
    img=models.FileField(upload_to='pic')


