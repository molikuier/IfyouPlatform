from django.contrib import admin

# Register your models here.
from index.models import Book,Author,UserInfo

admin.site.register([Book,Author,UserInfo])