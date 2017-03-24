from django.contrib import admin
from .models import UserModel, EventModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(EventModel)