from django.db import models

# Create your models here.
class reg(models.Model):
    Firstname=models.CharField(max_length=20,default="")
    Lastname = models.CharField(max_length=20,default="")
    Email=models.EmailField()

class EmojiModel(models.Model):
    emoji = models.CharField(max_length=10) 