from django.contrib import admin

from .models import DataProfessor

# Register your models here.

class DataProfessorAdmin(admin.ModelAdmin):
    list_display=('name_professor', 'course' ,'number_semester', 'content')
    readonly_fields=('created',)


admin.site.register(DataProfessor, DataProfessorAdmin)