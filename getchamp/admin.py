from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(TeamBuilder)
admin.site.register(Champion)
admin.site.register(Item)