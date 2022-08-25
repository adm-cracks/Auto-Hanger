from distutils.command.upload import upload
from django.db import models

# Create your models here.

class brands(models.Model):
    b_name = models.CharField(max_length=100)
    b_img = models.ImageField(upload_to ='pic')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.b_name
    
    
class parts(models.Model):
    brand = models.ForeignKey(brands,related_name='partss',on_delete=models.CASCADE)
    p_name = models.CharField(max_length=100)
    p_img = models.ImageField(upload_to ='pic')
    p_deta = models.TextField()
    p_price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.p_name