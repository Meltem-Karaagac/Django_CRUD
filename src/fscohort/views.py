from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student


def home_view(request):
    # print(request.GET.get("q"))
    # print(request.COOKIES)
    # print(request.user)
    # print(request.path)
    # print(request.method)
    # form = StudentForm()
    # my_context = {
    #     'title': '<b>clarusway</b>',
    #     'dict_1': {'djang': 'best framework'},
    #     'my_list': [2, 3, 4, 5],
    #     'cat': 'maviş',
    #     'student': form
    # }
    return render(request, "fscohort/home.html")

# Create your views here.


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, "fscohort/student_list.html", context)


def student_add(request):
    form = StudentForm()
    if request.method == "POST":
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, "fscohort/student_add.html", context)
