from django.shortcuts import render, HttpResponse, redirect
from .models import Info

# Create your views here.
def info(request):
    constant = {'success' : False}
    if request.method == "POST":
        name=request.POST['name']
        rollno=request.POST['rollno']
        print(name,rollno)
        ins=Info(name=name,rollno=rollno)
        ins.save()
        constant = {'success' : True}
        
    return render(request,'form.html',constant)


def data(request):
    allInfos= Info.objects.all()
    context = {'infos': allInfos}
    return render(request,'data.html',context)

def update(request, id):
    info = Info.objects.get( id = id)
    if request.method == "POST":
        info.name=request.POST['name']
        info.rollno=request.POST['rollno']
        info.save()   
        return redirect("/data")
    return render(request, 'update.html',{'info':info} )


def delete(request, id):
    info = Info.objects.get(id = id)
    info.delete()
    return redirect('/data')