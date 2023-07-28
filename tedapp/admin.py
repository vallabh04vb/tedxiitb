from django.contrib import admin
from . import models
from tedapp.models import UserAccount
# Register your models here.
admin.site.register(UserAccount)