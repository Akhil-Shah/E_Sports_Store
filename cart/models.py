from django.db import models

# Create your models here.

class Feedback(models.Model):
    purchase_id = models.UUIDField(primary_key = True)
    email = models.CharField(max_length=50,null=False,blank=False)
    phone = models.IntegerField()
    feedback = models.CharField(max_length=100,null=False,blank=False)
