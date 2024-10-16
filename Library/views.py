from django.shortcuts import render
from Library.models import Student,Book,Borrowing,Course,Mentor
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):

    context = {
        'firstname': 'Siuuu',
        'greeting' : 0,
    }
    return render (request,"index.html",context)

def view(request):
    context = {
        'firstname': 'Siuuu',
    }
    return render (request,"view.html",context)



def database(request):
    student = Student.objects.all().values()
    book = Book.objects.all().values()
    borrowing = Borrowing.objects.all().values()
    course = Course.objects.all().values()

    
    context = {
        'data1' : student,
        'data2' : book,
        'data3' : borrowing,
        'data4' : course,
    }
    return render (request,"database.html",context)




def course(request):
    course = Course.objects.all().values()

    if request.method == "POST":
        c_code = request.POST['code']
        c_desc = request.POST['desc']
        data=Course(code=c_code, description=c_desc)
        data.save()

    context = {
        'allcourse' : course,
    }        
    return render (request,("course.html"),context)


def mentor(request):
    mentor = Mentor.objects.all().values()

    if request.method == "POST":
        id = request.POST['menid']
        name = request.POST['menname']
        roomno = request.POST['menroomno']
        data=Mentor(menid=id, menname=name, menroomno=roomno)
        data.save()

    context = {
        'data' : mentor , 
    }
    return render (request,"newmentor.html",context)


def update_course(request,code):
    data=Course.objects.get(code=code)
    context={
        'data':data
    }
    return render (request , "update_course.html", context)


def save_update_course(request,code):
    c_desc= request.POST['desc']
    data=Course.objects.get(code=code)
    data.description = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))



def update_mentor(request,menid):
    data=Mentor.objects.get(menid=menid)
    context={
        'data':data
    }
    return render (request , "update_mentor.html", context)


def save_update_mentor(request,menid):
    menname = request.POST['name']
    menroomno = request.POST['roomno']
    data=Mentor.objects.get(menid=menid)
    data.menname = menname 
    data.menroomno = menroomno
    data.save()
    return HttpResponseRedirect(reverse("newmentor"))

def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse("course"))

def delete_mentor(request,menid):
    data = Mentor.objects.get(menid=menid)
    data.delete()
    return HttpResponseRedirect(reverse("newmentor"))


def search_course(request):
    if request.method == "GET":
        c_code = request.GET.get('c_code')
    
        if c_code:
            data = Course.objects.filter(code=c_code)

        else:
            data = None
    
        context = {
         'data': data
        }
        return render(request, "search_course.html", context)
    
    return render(request, "search_course.html")
