from django.shortcuts import render,HttpResponseRedirect
from enroll.forms import Student_Model,Student_Form
# from django.http import HttpRequestRedirect

# Create your views here.
def add_show(request):
    if request.method == "POST":
        sf = Student_Form(request.POST)
        if sf.is_valid():
            na = sf.cleaned_data['name']
            em = sf.cleaned_data['email']
            pw = sf.cleaned_data['password']
            print(na)
            print(em)
            print(pw)
            sm_obj = Student_Model(name=na, email=em, password=pw)
            sm_obj.save()
            sf = Student_Form()
    else:
        sf = Student_Form()

    sm = Student_Model.objects.all()
    students = {
        'sm': sm,
        'sf': sf,
    }
    return render(request, "enroll/home.html", students)


def delete(request, id):
    if request.method == "POST":
        sm_obj = Student_Model.objects.get(pk=id)
        sm_obj.delete()
        return HttpResponseRedirect("/")

def update(request, id):
    if request.method == "POST":
        pi = Student_Model.objects.get(pk=id)
        sf = Student_Form(request.POST, instance=pi)
        if sf.is_valid():
            sf.save()
            return HttpResponseRedirect("/")
    else:
        pi = Student_Model.objects.get(pk=id)
        sf = Student_Form(instance=pi)

    students = {
        'sf': sf,
    }
    return render(request, "enroll/update.html", students)
    