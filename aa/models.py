from django.db import models





class Rooms(models.Model):
    name = models.CharField(max_length=23,blank=True,null=True)
    username1=models.CharField(max_length=11)
    username2=models.CharField(max_length=11,null=True,default=None)
    