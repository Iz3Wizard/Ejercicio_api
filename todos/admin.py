from django.contrib import admin

# Register your models here.
from  .models import Task
from django.db import models

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    search_fields =('title','body')
    list_filter = ( 'title', 'body')
    list_per_page = 10
  
    
    
    
    
admin.site.register(Task, TaskAdmin)