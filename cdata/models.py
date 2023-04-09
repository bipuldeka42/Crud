from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=200)
    cl=models.CharField(max_length=200)
    roll=models.IntegerField()
    pro_img=models.ImageField(upload_to='pro')
    def __str__(self):
        return self.name
class Image(models.Model):
    name=models.CharField(max_length=30)
    img=models.ImageField(upload_to='pro')
    
    
