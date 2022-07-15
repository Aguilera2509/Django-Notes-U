from django.shortcuts import render, redirect
from .models import DataProfessor
import re

# Create your views here.

def main(request):

    allData = DataProfessor.objects.all()

    if request.method == 'POST':
        form = request.POST

        messages_err = {
            'name': None,
            'semester': None,
            'comment': None,
        }

        if re.findall('[0-9^¡!.¿?@#&_*$=%*:;<>+-/\|""'',]', form['nameProf']) or len(form['nameProf']) < 3:
            messages_err['name'] = "El nombre introducido NO es valido"

        if int(form['semester']) <= 0 or int(form['semester']) >= 11 or len(form['semester']) == 0:
            messages_err['semester'] = "El numero del semestre NO es valido"

        if len(form['comment']) > 300 or len(form['comment']) < 8:
            messages_err['comment'] = "El comentario debe ser menos a 300 y mayor a 8 caracteres"

        if messages_err['name'] != None or messages_err['semester'] != None or messages_err['comment'] != None:
            return render(request,'index.html', {'allData':allData, 'err': messages_err})
        
        data = DataProfessor()

        data.name_professor = form['nameProf']
        data.course = form['areaProf']
        data.number_semester = form['semester']
        data.content = form['comment']

        data.save()
    
    return render(request,'index.html', {'allData':allData})