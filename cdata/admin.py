from django.contrib import admin

from .models import Students

# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
  list_display = ("id","name", "cl", "roll",'pro_img')
  
admin.site.register(Students, StudentsAdmin)
