from django.contrib import admin
from .models import Task

# Register your models here.
class Admin_list(admin.ModelAdmin):
    list_display=("task","Is_completed","Updated_at","Created_at")
    search_fields=("task" ,)

admin.site.register(Task , Admin_list)