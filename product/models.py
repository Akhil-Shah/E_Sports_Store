from django.db import models

from django.urls import reverse
# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=10,null=False,blank=False)
    back_img_url = models.CharField(default="",max_length=100)

    def get_absolute_url(self):
        return reverse('product:team_names', kwargs={'name': self.name})
    
class Team(models.Model):
    name = models.CharField(max_length=10,null=False,blank=False)
    game = models.ForeignKey(Game,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('product:item_names', kwargs={'name': self.name})

class Item(models.Model):
    name = models.CharField(max_length=10,null=False,blank=False)
    price = models.IntegerField(default=50)
    img_url = models.CharField(default="",max_length=100)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)