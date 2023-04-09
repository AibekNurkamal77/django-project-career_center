from django.contrib import admin

from .models import Teacher_Post

class Teacher_Post_Admin(admin.ModelAdmin):
    list_display = ['name', 'surname']


admin.site.register(Teacher_Post, Teacher_Post_Admin)