from django.contrib import admin

# Register your models here.

from .models import *

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass
