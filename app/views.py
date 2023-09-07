from django.shortcuts import render
from app.models import *
#from django.http import HttpResponse
# Create your views here.
def insert_school(request):
    if request.method=="POST":
        #request.POST={'scn':SV,'sp':SV,'sl':SV}
        scn =request.POST['scn']
        scp = request.POST['scp']
        scl = request.POST['scl']

        so = school.objects.get_or_create(scname=scn,scprincipal=scp,sclocation=scl)[0]
        so.save()
        qlso=school.objects.all()
        d = {'qlso':qlso}   
        return render(request,'display_school.html',d)
    
    return render(request,'insert_school.html')

def insert_student(request):
    if request.method == 'POST':
        sln = request.POST['sln']
        stn = request.POST['stn']
        sid = request.POST['sid']

        so = school.objects.get(scname=sln)
        dw = student.objects.get_or_create(scname=so,stname=stn,stid=sid)[0]
        dw.save()
        qsio = student.objects.all()
        d = {'qsio':qsio}
        return render(request,'display_student.html',d)
    
    return render(request,'insert_student.html')