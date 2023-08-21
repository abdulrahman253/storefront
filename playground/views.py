from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    name = request.GET.get('name' ,'ahmed')
    return render(request , 'hello.html',{'name' : name})
