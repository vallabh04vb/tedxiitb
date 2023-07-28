from django.db import models

# Create your models here.

class UserAccount(models.Model):
    name = models.CharField(max_length=200, default="")
    email = models.CharField( max_length=254 , default="")
    phone = models.IntegerField(default=0)
    referral = models.CharField( max_length=50, default = "")
    City = models.CharField( max_length=50, default = "")
    college = models.CharField( max_length=200, default = "")
  

    def __str__(self):
        return self.name