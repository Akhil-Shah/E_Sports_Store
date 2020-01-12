from django.contrib import admin

from .models import (
    Game,
    Team,
    Item,
)
# Register your models here.

myModels = [Game,Team,Item]
admin.site.register(myModels)