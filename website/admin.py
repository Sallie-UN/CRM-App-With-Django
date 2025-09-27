from django.contrib import admin
from .models import Record
# Register your models here.
admin.site.register(Record)
# You have to import the model you create and register it here in the admin.py file  - else it won't be visible in the admin database