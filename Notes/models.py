from django.db import models

# Create your models here.

class DataProfessor(models.Model):
    name_professor=models.CharField(max_length=26)
    number_semester=models.IntegerField()
    course=models.CharField(max_length=20, default=0)
    content=models.CharField(max_length=300)
    created=models.DateTimeField(auto_now_add=True)