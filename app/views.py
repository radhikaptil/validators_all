from urllib.error import HTTPError
from django.shortcuts import render

# Create your views here.
from app.forms import StudentForm
from django.http import HttpResponse

def insert_student(request):
    SEFO=StudentForm()
    d={'SEFO':SEFO}

    if request.method=='POST':
        SDFO=StudentForm(request.POST)
        if SDFO.is_valid():

            return HttpResponse(str(SDFO.cleaned_data))
        else:
            return HttpResponse('Invalid data')
        
    return render(request,'insert_student.html',d)