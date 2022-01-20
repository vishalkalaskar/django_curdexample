from django.shortcuts import render,redirect
from . models import Employee
from django.db.models import F
def showindex(request):
    return render(request,'common/index.html')

def save(request):
    if request.method == "POST":
        eid = request.POST.get("eid")
        ename = request.POST.get("ename")
        eemail = request.POST.get("eemail")
        econtact = request.POST.get("econtact")

        Employee(eid=eid,ename=ename,eemail=eemail,econtact=econtact).save()
        info=Employee.objects.all()
        return render(request,'common/show.html',{'emp':info})
        # return redirect('/save', {'emp':info})
    else:
       return render(request,'common/show.html',{'emp':Employee.objects.all()})

def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return render(request,'common/show.html',{"emp":Employee.objects.all()})

def update(request,id):
    if request.method == "POST":

        eid = request.POST.get("eid")
        ename = request.POST.get("ename")
        eemail = request.POST.get("eemail")
        econtact = request.POST.get("econtact")

        Employee.objects.filter(eid=eid).update(eid=eid, ename=ename, eemail=eemail, econtact=econtact)


        return render(request, 'common/show.html', {'emp': Employee.objects.all()})
    else:
       return render(request, 'common/update.html',{'employee':Employee.objects.get(id=id)})