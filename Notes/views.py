from django.shortcuts import render, redirect
from .models import DataProfessor

# Create your views here.

def main(request):

    allData = DataProfessor.objects.all()

    if request.method == 'POST':
        form = request.POST

        data = DataProfessor()

        data.name_professor = form['nameProf']
        data.course = form['areaProf']
        data.number_semester = form['semester']
        data.content = form['comment']

        data.save()
    
        return redirect('main')

    
    return render(request,'index.html', {'allData':allData})