from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm


def home_view(request):
    # print(request.GET.get("q"))
    # print(request.COOKIES)
    # print(request.user)
    # print(request.path)
    # print(request.method)
    form = StudentForm()
    my_context = {
        'title': '<b>clarusway</b>',
        'dict_1': {'djang': 'best framework'},
        'my_list': [2, 3, 4, 5],
        'cat': 'maviş',
        'student': form
    }
    return render(request, "fscohort/home.html", my_context)

# Create your views here.


def about(request):
    return HttpResponse("About page.")
